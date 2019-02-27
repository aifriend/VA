import json
import logging
import sys
import requests

from config import Config
from flask import Flask, request
from service.manager.RPADialogManager import RPADialogManager
from service.manager.SAPDialogManager import SAPDialogManager
from tools.response_utils import make_business_response
from tools.ACNLogger import ACNLogger

app = Flask(__name__)
logger = ACNLogger(name="BusinessLogic", file="logs/app-buslog.log")


@app.route('/sap_service', methods=['POST'])
def sap_service():
    payload = request.json

    if isinstance(payload, str):
        payload = json.loads(payload)

    sap_manager = SAPDialogManager()
    answer = sap_manager.get_answer(payload['service'], payload['session'])

    return make_business_response(answer, 200)


@app.route('/rpa_service', methods=['POST'])
def rpa_service():
    payload = request.json

    if isinstance(payload, str):
        payload = json.loads(payload)

    rpa_manager = RPADialogManager()
    answer = rpa_manager.get_answer(payload['service'], payload['session'])

    return make_business_response(answer, 200)


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
            req_config = req_config.get('BUSINESS')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
