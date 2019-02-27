import json
import logging
import sys
import requests

from config import Config
from watson_assistant.RepoComponentsFactory import RepoComponentsFactory
from flask import Flask, request
from tools.response_utils import make_repo_response
from tools.ACNLogger import ACNLogger
from tools.response_utils import make_repo_error_response

app = Flask(__name__)
logger = ACNLogger(name="WatsonService", file="logs/app-repo.log")

global actual_token


@app.route('/exec_repo', methods=['GET', 'POST'])
def exec_repo():
    body = request.json

    if isinstance(body, str):
        body = json.loads(body)

    global actual_token
    session = body['session']

    # Query service
    try:
        wd_service = RepoComponentsFactory().get_wd_service()
        status, reason, answer = wd_service.execute_wd(actual_token, session, body['query'])
        if status != 200:
            actual_token = _update_token(session)
            status, reason, answer = wd_service.execute_wd(actual_token, session, body['query'])
    except:
        return make_repo_error_response("WA not available", 400)

    logger.debug(session, "exec_repo - Response: {0} - {1}".format(status, answer))

    return make_repo_response(answer, 200)


def _update_token(session):
    new_token = ""

    # Login service
    auth_service = RepoComponentsFactory().get_auth_service()
    status, reason, answer = auth_service.get_oauth_token(session)

    # Authentication OK
    if status == 200:
        new_token = answer

    logger.debug(session, "update_token - Response: {0}".format(new_token))

    return new_token


def _get_module_config():
    config_endpoint = Config.CONFIG_MODULE_ENDPOINT

    # Request
    headers = {
        'content-type': "application/json"
    }

    # Response
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

    actual_token = ""

if __name__ == "__main__":
    try:
        actual_token = ""
        req_config = _get_module_config()
        if len(req_config) > 0:
            req_config = req_config.get('WA')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
