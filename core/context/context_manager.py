import logging
import sys
import requests
import json

from config import Config
from flask import Flask, request
from tools.response_utils import make_context_error_response, make_context_response, make_context_error_logic_response
from service.context.Stack import Stack
from tools.ACNLogger import ACNLogger

app = Flask(__name__)
logger = ACNLogger(name="ContextManager", file="logs/app-context.log")

local_db = {}

CONVERSATION_LABEL = "conversation"


@app.route('/update_logs/<session>/<key>/<value>', methods=['POST'])
def update_logs(session, key, value):
    global local_db

    if session not in local_db.keys():
        return make_context_error_logic_response({"Error": "conversation history not found"}, 400)

    # update last conversation of the actual session
    history_item = local_db[session].pop()
    history_item[CONVERSATION_LABEL][key] = value
    local_db[session].push(history_item)

    logger.debug(session, 'update_logs: {0}'.format(local_db))

    return make_context_response({"OK": "OK"}, 200)


@app.route('/send_logs', methods=['POST'])
def send_logs():
    content = request.json

    if isinstance(content, str):
        content = json.loads(content)

    _add_log(content)

    return make_context_response({"OK": "OK"}, 200)


def _add_log(content):
    global local_db

    session = content["session"]
    question = content["question"]
    answer = content["answer"]
    intent = content["intent"]
    entities = content["entities"]
    locale = content["locale"]
    authorization = content["authorization"]

    # conversation item
    history_item = {
        CONVERSATION_LABEL: [
            {"question": question},
            {"answer": answer},
            {"intent": intent},
            {"entities": entities},
            {"locale": locale},
            {"authorization": authorization}
        ]
    }

    # create new session for history logs
    if session not in local_db.keys():
        local_db[session] = Stack()

    # log conversation
    local_db[session].push(history_item)


@app.route('/get_back_logs/<session>/<backtrack>/', methods=['GET'])
def get_back_logs(session, backtrack=0):
    global local_db

    try:
        # create new session for history logs
        if session not in local_db.keys():
            local_db[session] = Stack()
            logs = []

        elif backtrack == '-1':
            # guess last historic conversation with intent
            logs = local_db[session].find(CONVERSATION_LABEL, "intent", lambda a: a)

        else:
            logs = local_db[session].peek(backtrack)

    except:
        logger.exception("Exception: {0}".format(local_db))
        return make_context_error_logic_response({"Error": "conversation history backtraking error"}, 400)

    return make_context_response(logs, 200)


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
            req_config = req_config.get('CONTEXT')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
