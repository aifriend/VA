import json
import requests

from service.manager.IDialogManager import IDialogManager
from tools.ACNLogger import ACNLogger


class BusinessLogicDialogManager(IDialogManager):
    """Handles request to Business Logic Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="BusinessLogicDialogManager", file="logs/businesslogic-dialog.log")
        self.req_config = self.req_config.get('BUSINESS')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        self.endpoint = 'http://' + url + ':' + port + '/'

    def get_answer(self, question, session=None, extra_parameters=None):
        """Returns formatted JSON with repository response.

        Args:
            question: requested action
            session: user session information
            extra_parameters: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        """
        answer = self._get_action(session)

        return answer

    def _get_action(self, session):
        # Request
        answer = {"action": session}
        headers = {
            'content-type': "application/json"
        }

        # Response with
        payload = json.dumps(answer)
        response = requests.request("POST", self.endpoint, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(session, "get_action - response: {0}".format(response))

        return response
