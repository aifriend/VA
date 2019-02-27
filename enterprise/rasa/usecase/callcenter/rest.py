from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import logging

from context.RasaContext import RasaContext
from flask import Blueprint, request
from rasa_core.channels import InputChannel, UserMessage
from tools.response_utils import make_rasa_response, make_rasa_error_response, make_rasa_error_logic_response


class HttpInputComponent(InputChannel):

    @classmethod
    def name(cls):
        return "rasaio"

    def blueprint(self, on_new_message):
        """Defines a Flask blueprint.

        The blueprint will be attached to a running flask server and handel
        incoming routes it registered for.

        Response
            "answer": {
                "session": session,
                "response": response
            }

        """
        rasa_webhook = Blueprint('rasa_webhook', __name__)

        @rasa_webhook.route("/", methods=['POST'])
        def receive():
            try:
                content = request.json

                if isinstance(content, str):
                    content = json.loads(content)

                rasa_rest = RasaContext.from_request(content)
                text = rasa_rest.process_rest()
                rasa_response = on_new_message(UserMessage(str(text), None, rasa_rest.session))

                if not(rasa_response is None) and isinstance(rasa_response, list) and len(rasa_response) > 0:
                    try:
                        return make_rasa_response(rasa_response, 200)
                    except:
                        return make_rasa_error_response("RASA Response Error", 400)
                else:
                    return make_rasa_error_logic_response("RASA Blank Response", 300)

            except ValueError as e:
                logging.exception(e)
                return make_rasa_error_logic_response("RASA Value Error", 400)

            except Exception as exc:
                logging.exception(exc)
                return make_rasa_error_response("RASA Internal Server Error", 500)

        return rasa_webhook
