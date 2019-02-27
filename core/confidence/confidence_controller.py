import json
import logging
import sys
import requests

from config import Config
from flask import Flask, request
from tools.response_utils import make_confidence_response, make_confidence_error_logic_response
from tools.ACNLogger import ACNLogger

app = Flask(__name__)
logger = ACNLogger(name="ConfidenceController", file="logs/app-confid.log")
config_data = []


@app.route('/entity_upper_confidence', methods=['POST'])
def entity_upper_confidence():
    content = request.json

    if isinstance(content, str):
        content = json.loads(content)

    confidence = content["confidence"]
    entity = content["entity"]

    priority = config_data["data"]
    try:
        try:
            entity_priority = priority["ENTITY_PRIORITY_TABLE"][entity]
        except:
            entity_priority = "Low"

        threshold = priority["THRESHOLD_TABLE"][entity_priority]
        res = confidence >= float(threshold[0]["ENT_upper_threshold"])

        return make_confidence_response(res, 200)

    except:
        response = {"threshold": False, "reason": "Entity upper confidence"}
        logger.exception("Exception: {0}".format(response))
        return make_confidence_error_logic_response(response, 400)


@app.route('/entity_lower_confidence', methods=['POST'])
def entity_lower_confidence():
    content = request.json

    if isinstance(content, str):
        content = json.loads(content)

    confidence = content["confidence"]
    entity = content["entity"]

    priority = config_data["data"]
    try:
        try:
            entity_priority = priority["ENTITY_PRIORITY_TABLE"][entity]
        except:
            entity_priority = "Low"

        threshold = priority["THRESHOLD_TABLE"][entity_priority]
        res = confidence <= float(threshold[0]["ENT_lower_threshold"])

        return make_confidence_response(res, 200)

    except:
        response = {"threshold": False, "reason": "Entity lower confidence"}
        logger.exception("Exception: {0}".format(response))
        return make_confidence_error_logic_response(response, 400)


@app.route('/intent_upper_confidence', methods=['POST'])
def intent_upper_confidence():
    content = request.json

    if isinstance(content, str):
        content = json.loads(content)

    confidence = content["confidence"]
    intent = content["intent"]

    priority = config_data["data"]
    try:
        try:
            intent_priority = priority["INTENT_PRIORITY_TABLE"][intent]
        except:
            intent_priority = "Low"

        threshold = priority["THRESHOLD_TABLE"][intent_priority]
        res = confidence >= float(threshold[0]["INT_upper_threshold"])

        return make_confidence_response({"threshold": res}, 200)

    except:
        response = {"threshold": False, "reason": "Intent upper confidence"}
        logger.exception("Exception: {0}".format(response))
        return make_confidence_error_logic_response(response, 400)


@app.route('/intent_lower_confidence', methods=['POST'])
def intent_lower_confidence():
    content = request.json

    if isinstance(content, str):
        content = json.loads(content)

    confidence = content["confidence"]
    intent = content["intent"]

    priority = config_data["data"]
    try:
        try:
            intent_priority = priority["INTENT_PRIORITY_TABLE"][intent]
        except:
            intent_priority = "Low"

        threshold = priority["THRESHOLD_TABLE"][intent_priority]
        res = confidence <= float(threshold[0]["INT_lower_threshold"])

        return make_confidence_response({"threshold": res}, 200)

    except:
        response = {"threshold": False, "reason": "Intent lower confidence"}
        logger.exception("Exception: {0}".format(response))
        return make_confidence_error_logic_response(response, 400)


def _get_confidence_config():
    config_endpoint = Config.CONFIG_CONFIDENCE_ENDPOINT

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


def _get_endpoint_config():
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

    config_data = _get_confidence_config()

if __name__ == "__main__":
    try:
        config_data = _get_confidence_config()
        req_config = _get_endpoint_config()
        if len(req_config) > 0:
            req_config = req_config.get('CONFIDENCE')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
