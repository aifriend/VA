import json
import logging
import sys
import requests

from config import Config
from service.ComponentsFactory import ComponentsFactory
from service.context.ContextData import ContextData
from service.manager.ContextDialogManager import ContextActionMode
from service.manager.SecurityDialogManager import SecurityService
from flask import request, Flask
from tools.response_utils import \
    make_dialog_error_auth_response, \
    make_dialog_response, \
    make_dialog_error_response, \
    make_faq_dialog_response, \
    make_default_dialog_response
from tools.ACNLogger import ACNLogger

app = Flask(__name__)
logger = ACNLogger(name="DialogManager", file="logs/app-dialog.log")

security_manager = ComponentsFactory.get_security_dialog_manager()
context_manager = ComponentsFactory.get_context_dialog_manager()
repo_manager = ComponentsFactory.get_repository_dialog_manager()
nlu_manager = ComponentsFactory.get_natural_language_understander()
dialog_controller = ComponentsFactory.get_rasa_dialog_manager()


@app.route('/get_answer', methods=['POST'])
def get_repo_answer():
    try:
        content = request.json

        if isinstance(content, str):
            content = json.loads(content)

        if content:
            # Request content
            session = content['request']['session']
            question = content['request']['transcription']

            # Context
            context_data = ContextData(session, question=question)

            # Client authorization
            _ = security_manager.get_answer(context_data)
            if context_data.authorization != "OK":
                return make_dialog_error_auth_response(context_data.authorization,
                                                       session=session, status_code=400)

            # call Repository Service first (FAQ request)
            faq_response = repo_manager.get_answer(context_data)

            # main control loop
            if not faq_response:

                # Level authorization
                flow_allowed = security_manager.get_answer(context_data, SecurityService.GET_FLOW)
                if flow_allowed["result"] != "OK":
                    return make_dialog_error_auth_response(context_data.authorization,
                                                           session=session, status_code=400)

                # NLU intent/entities confidence thresholding filter (remove intent/entity below threshold)
                _ = nlu_manager.get_answer(context_data)

                # Context intent resolver
                _ = context_manager.get_answer(context_data, ContextActionMode.RESOLVER)

                # Call dialog control manager
                payload = dialog_controller.get_answer(context_data)
                res = make_dialog_response(payload)

            else:
                # FAQ response
                res = make_faq_dialog_response(context_data)

            # Track context
            _ = context_manager.get_answer(context_data)

            return res

        else:
            return make_dialog_error_response("Ups! Querías decirme algo?")

    except Exception as exc:
        return make_dialog_error_response("Ups! Me pillas distraido! Que me estabas diciendo? ... ".format(exc))


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
            req_config = req_config.get('DIALOG')
            app.run(debug=True, host=str(req_config.get('url')), port=int(req_config.get('port')))
        else:
            logger.warning("", "Endpoint unavailable")
    except:
        logger.exception("Exception: Endpoint unavailable")
