import json
import logging
import sys
import requests

from config import Config
from flask import Flask, request
from service.SapService import SapService
from tools.response_utils import make_sap_response
from tools.ACNLogger import ACNLogger

app = Flask(__name__)
logger = ACNLogger(name="SapService", file="logs/app-sap.log")


@app.route('/sap_ws', methods=['POST'])
def sap_ws():
    service_data = request.json

    if isinstance(service_data, str):
        service_data = json.loads(service_data)

    sap_manager = SapService()
    response = sap_manager.call_service(service_data)

    return make_sap_response(response, 200)


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
            req_config = req_config.get('SAP_DEV')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
