import json
import requests

from manager.IDialogManager import IDialogManager
from tools.ACNLogger import ACNLogger


class BusinessDialogManager(IDialogManager):
    """Handles request to Business Logic Service.
    """
    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="BusinessDialogManager", file="logs/rasa-action-server.log")
        self.req_config = self.req_config.get('BUSINESS')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        self.endpoint = 'http://' + url + ':' + port

    def get_answer(self, service_selector, user_id=None, service_instance=None):
        """Returns formatted JSON with repository response.

        Args:
            service_selector: requested action
            user_id: user session information
            service_instance: service instance

        """
        s = Selector(self.endpoint, user_id, self.logger)
        answer = s.get_mode(service_selector, service_instance)

        return answer


class Selector(object):
    """Handles Business Logic Action Selections.
    """
    def __init__(self, blogic_root, session, logger):
        self.root_endpoint = blogic_root
        self.session = session
        self.logger = logger
        self.service = {}

    def get_mode(self, action, service):
        self.service = service
        method_name = 'blogic_' + str(action).lower()
        method = getattr(self, method_name, lambda: 'Selector')
        return method()

    def blogic_rpa(self):
        return self._get_action(self.root_endpoint + "/rpa_service")

    def blogic_sap(self):
        return self._get_action(self.root_endpoint + "/sap_service")

    def _get_action(self, endpoint):
        # Request
        answer = {
            "session": self.session,
            "service": self.service.__dict__
        }
        headers = {
            'content-type': "application/json"
        }

        # Response with
        payload = json.dumps(answer)
        response = requests.request("POST", endpoint, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(self.session, "get_action - Response: {0}".format(response))

        try:
            if response is not None:
                # Response status
                status = response['result']
                if status != "OK":
                    # Update context
                    response['response'] = "SAP not available!"
                    return response
                elif not response['response']:
                    response['response'] = "SAP empty!"
                    return response

        except:
            self.logger.exception("Exception: Business - get_action")

        return response

