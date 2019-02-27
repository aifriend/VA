import logging
import sys
import requests
import json

from config import Config
from service.RpaComponentsFactory import RpaComponentsFactory
from flask import Flask, request
from tools.response_utils import make_rpa_response
from tools.ACNLogger import ACNLogger

app = Flask(__name__)
logger = ACNLogger(name="RpaService", file="logs/app-rpa.log")


def call_r000484(token, pars):
    call_result = "ERROR"
    call_reason = ""

    aros = RpaComponentsFactory().get_aros_service()
    sqs = RpaComponentsFactory().get_sqs_service()

    # pars = "Acreedor=1191522;NIF=33434194Z;OrgCompras=6008;Moneda=EUR".split(';')

    if 'Acreedor' in pars and \
            'NIF' in pars and \
            'OrgCompras' in pars and \
            'Moneda' in pars and \
            'CondPago' in pars and \
            'Usuario' in pars:

        robot_params = ["Acreedor=%s" % pars['Acreedor'], "NIF=%s" % pars['NIF'], "OrgCompras=%s" % pars['OrgCompras'],
                        "Moneda=%s" % pars['Moneda'], "CondPago=%s" % pars['CondPago'], "Usuario=%s" % pars['Usuario']]

        robot_id = req_config.get('robot_id')
        status, reason, robotinfo = aros.get_robot_info(token, robot_id)
        if status == 200:
            robotjson = json.loads(robotinfo.decode('UTF-8'))
            if robotjson['State'] == 0:
                status, reason, _ = aros.execute_robot(token, robot_id, robot_params)
                if status == 204:  # RPA Requested OK
                    call_result = 'OK'
                elif status == 401:  # Unauthorized
                    call_reason = 'Authorization has been denied for this request.'
                else:
                    call_reason = reason
            else:
                account_id = req_config.get('login_account')
                account_queue = req_config.get('login_queue')
                status, reason, robotinfo = sqs.send_sqs_message(account_id, account_queue, ';'.join(robot_params))
                if status == 200:
                    call_result = 'OK'
                    call_reason = 'QUEUED'
                else:
                    call_reason = reason
        else:
            call_reason = reason
    else:
        call_result = "ERROR"
        call_reason = "Required parameters not found"

    logger.debug("UNDEFINED", "RpaService - call_r000484: {0}.{1}".format(call_result, call_reason))

    return call_result, call_reason


def _parse_answer(response):
    try:
        if response['result'] == 'OK':
            if response['response'] == "":
                transcript = ("Su petición ha sido tramitada correctamente, en cuanto sea terminada"
                              "se lo confirmaremos por correo electrónico.")
            elif response['response'] == "QUEUED":
                transcript = ("Su petición se ha puesto en cola para procesarse, en cuanto sea realizada"
                              "se lo confirmaremos por correo electrónico.")
            else:
                transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                              "En caso de persistir el error contacto con ISI_SOPORTE.")

        elif response['result'] == 'ERROR':
            transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo más tarde."
                          "En caso de persistir el error contacto con ISI_SOPORTE.")

        else:
            transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                          "En caso de persistir el error contacto con ISI_SOPORTE.")
    except:
        transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                      "En caso de persistir el error contacto con ISI_SOPORTE.")

    message = {
        "type": "",
        "id": "",
        "transcript": transcript
    }

    return message


@app.route('/exec_rpa', methods=['POST'])
def exec_rpa():
    req_config = request.json

    if isinstance(req_config, str):
        req_config = json.loads(req_config)

    user = req_config.get('user')
    passwd = req_config.get('password')

    aros = RpaComponentsFactory().get_aros_service()

    res = {'robot_id': '', 'result': 'ERROR', 'reason': ''}

    status, reason, resp = aros.get_oauth_token(user, passwd)
    if status == 200:  # Authentication OK
        token = json.loads(resp.decode('UTF-8'))['access_token']
        body = request.json
        res['robot_id'] = body['robot']
        if res['robot_id'] == req_config.get('robot_name'):
            result, reason = call_r000484(token, body['params'])
            res['result'] = result
            res['reason'] = reason
        else:
            res['reason'] = "Robot code not defined"
    elif status == 400:  # Bad Request
        res['reason'] = json.loads(resp.decode('UTF-8'))['error_description']
    else:
        res['reason'] = reason

    # Use case response filter
    # res = _parse_answer(res)
    logger.debug("UNDEFINED", "RpaService - call_r000484: {0}".format(res['reason']))

    return make_rpa_response(res, 200)


def _get_module_config():
    config_endpoint = Config.CONFIG_MODULE_ENDPOINT

    # Request
    headers = {
        'content-type': "application/json"
    }

    # Response with
    try:
        config_response = requests.request("GET", config_endpoint, headers=headers)
        config_response.raise_for_status()
        config_response = json.loads(config_response.text)
    except:
        sys.exit('...Run Configuration Service first!')

    return config_response


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    try:
        req_config = _get_module_config()
        if len(req_config) > 0:
            req_config = req_config.get('RPA')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
