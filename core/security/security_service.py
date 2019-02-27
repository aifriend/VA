import json
import logging
import sys
import requests

from enum import Enum
from config import Config
from flask import Flask, request
from service.authorization_service.AuthorizationService import AuthorizationService
from tools.response_utils import make_security_response
from tools.ACNLogger import ACNLogger

app = Flask(__name__)
logger = ACNLogger(name="SecurityService", file="logs/app-secu.log")


class Action(Enum):
    AUTH_BACKEND = "backend"
    AUTH_SAP = "sap"


@app.route('/authorization', methods=['POST'])
def get_authorization():
    body = request.json

    if isinstance(body, str):
        body = json.loads(body)

    auth_service = AuthorizationService()
    answer = auth_service.check_authorization(body['session'])
    logger.debug(body["session"], "get_authorization - response: {0}".format(answer))

    return make_security_response(answer, 200)


@app.route('/get_flow', methods=['POST'])
def get_flow():
    body = request.json

    if isinstance(body, str):
        body = json.loads(body)

    answer = _get_action_flow(body['intent'], body['level'])

    logger.debug(body["session"], "get_flow - response: {0}".format(answer))

    return make_security_response(answer, 200)


def _get_action_flow(intent, level):
    res = {'result': 'ERROR', 'response': ''}

    action = _get_flow(intent, level)

    res['result'] = "OK" if action in Action else "NOT_ACTION_AVAILABLE"
    res['response'] = action

    return res


def _get_flow(intent, level):
    # Check SAP access authorization
    sap_auth = True if intent == ('robotlaunch' or 'robotbegin') and level['sap'] == 'yes' else False

    # Select action type
    if sap_auth:
        # call client backend service with Rasa
        return Action.AUTH_SAP.value

    # Access allowed to backend except SAP Service
    return Action.AUTH_BACKEND.value


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
            req_config = req_config.get('SECURITY')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
