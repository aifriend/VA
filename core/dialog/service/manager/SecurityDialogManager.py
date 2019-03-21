import json
import requests

from enum import Enum
from service.manager.IDialogManager import IDialogManager
from tools.ACNLogger import ACNLogger


class SecurityService(Enum):
    AUTHORIZATION = 1
    GET_FLOW = 2


class SecurityDialogManager(IDialogManager):
    """Handles request to Security Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="SecurityDialogManager", file="logs/security-dialog.log")
        self.req_config = self.req_config.get('SECURITY')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        self.endpoint = 'http://' + url + ':' + port

    def get_answer(self, context_result, service_mode=SecurityService.AUTHORIZATION, extra_parameters=None):
        """Returns formatted JSON with Security response.

        Args:
            context_result: context information
            service_mode: security service mode
            extra_parameters: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        """
        answer = self._get_answer(context_result, service_mode)

        return answer

    def _authorization(self, context_result):
        """
        :param context_result:
        :return:
            A JSON with Security response information. For example,
            {
                "authorization": { "OK", txt_error }
                "level": [
                    {
                        "sap": { "yes", "no" }
                    }
                ]
            }

        """
        # Request
        answer = {
            "session": context_result.session
        }
        headers = {
            'content-type': "application/json"
        }

        # Response with
        url = self.endpoint + "/authorization"
        payload = json.dumps(answer)
        response = requests.request("POST", url, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(context_result.session, "Authorization - Response: {0}".format(payload))

        # Update context
        context_result.update_from_authorization_security_response(response)

        return response

    def _get_flow(self, context_result):
        """
        :param context_result:
        :return:
            A JSON with Business Logic response information. For example:
            {
                "result": { "OK", "NOK" }
                "response": { backend, sap, not_allowed }
            }

        """
        # Request
        answer = {
            "session": context_result.session,
            "intent": context_result.intent.name,
            "level": context_result.authorization_level
        }
        headers = {
            'content-type': "application/json"
        }

        # Response with
        url = self.endpoint + "/get_flow"
        payload = json.dumps(answer)
        response = requests.request("POST", url, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(context_result.session, "get_flow - Response: {0}".format(payload))

        # Update context
        context_result.update_from_flow_security_response(response["response"])

        return response

    def _get_answer(self, context_result, service_mode):
        try:
            if service_mode == SecurityService.AUTHORIZATION:
                response = self._authorization(context_result)
            else:
                response = self._get_flow(context_result)
            self.logger.debug(context_result.session, "get_answer - Response: {0}".format(response))

        except Exception as exc:
            self.logger.exception("Exception: Security - get_answer")
            return {"authorization": "NOK", "level": {}}

        return response
