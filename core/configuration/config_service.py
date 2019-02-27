import json
import logging
import os
import yaml

from config import Config
from flask import Flask, jsonify
from tools.response_utils import make_config_error_response, make_config_response, make_config_error_logic_response
from tools.ACNLogger import ACNLogger

app = Flask(__name__)
logger = ACNLogger(name="ConfigServer", file="logs/app-config.log")


@app.route('/get_confidence_config', methods=['GET'])
def get_confidence_config():
    try:
        confidence_file = _get_confidence_config()
        if len(confidence_file) > 0:
            confidence_json = json.dumps(confidence_file)
            confidence_data = json.loads(confidence_json)
            return jsonify(confidence_data)
        else:
            return jsonify("Confidence file is empty")

    except Exception as exc:
        logger.exception("", "Exception: Confidence file is empty")
        return make_config_error_logic_response(exc, 400)


def _get_confidence_config():
    try:
        query_answer = {}
        if os.path.exists('./general/usecases'):
            config_file = "confidence.yaml"
            yaml_data = yaml.load(open("./general/usecases/" + config_file).read())
            query_answer = yaml_data

        return query_answer

    except:
        logger.exception("", "Exception: confidence.yaml")
        raise


@app.route('/get_module_config', methods=['GET'])
def get_module_config():
    try:
        config_file = _get_module_config()
        if len(config_file) > 0:
            return jsonify(config_file)
        else:
            return None

    except Exception as exc:
        logger.exception("Exception: get_module_config")
        return make_config_error_logic_response(exc, 400)


def _get_module_config():
    try:
        query_answer = {}
        if os.path.exists('./general'):
            config_file = "module_config-dev.json" if Config().isDev() else "module_config-pro.json"
            json_data = json.loads(open("./general/" + config_file).read())
            query_answer = json_data

        return query_answer

    except:
        logger.exception("Exception: module_config.json")
        raise


if __name__ != "__main__":
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == "__main__":
    req_config = _get_module_config()
    try:
        if len(req_config) > 0:
            req_config = req_config.get('CONFIG')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
