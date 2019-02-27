import json
import requests

from service.manager.IDialogManager import IDialogManager
from tools.ACNLogger import ACNLogger


class RPADialogManager(IDialogManager):
    """Handles request to RPA Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="RPADialogManager", file="logs/rpa-business.log")
        self.req_config = self.req_config.get('RPA')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        self.endpoint = 'http://' + url + ':' + port + '/exec_rpa'

    def get_answer(self, rpa_request, session=None, extra_parameters=None):
        """Returns formatted JSON with RPA response.

        Args:
            rpa_request: object with RASA information
            session: user session information
            extra_parameters: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A JSON with RPA response information.
            {
                "response": [OK, ERROR],
                "reason": [QUEUED,...]
            }
        """
        answer = self._get_answer(session, rpa_request)

        return answer

    def _get_answer(self, session, data):
        # Request
        answer = {"robot": data.robot_name, "params": {}}
        answer["params"]["Usuario"] = data.user_name
        answer["params"]["Acreedor"] = data.creditor
        answer["params"]["NIF"] = data.cnn
        answer["params"]["OrgCompras"] = data.buy_org
        answer["params"]["Moneda"] = data.currency
        answer["params"]["CondPago"] = data.pay_cond
        headers = {'content-type': "application/json"}

        # Response
        try:
            response = requests.request("POST", self.endpoint, data=json.dumps(answer), headers=headers)
            response.raise_for_status()
            answer_dm = json.loads(response.text)

        except:
            answer_dm = {'result': 'ERROR', 'reason': "RPA Get answer"}
            self.logger.exception("Exception: {0}".format(answer_dm))

        return self._parse_answer(answer_dm)

    @staticmethod
    def _parse_answer(response):
        try:
            if response['result'] == 'OK':
                if response['reason'] == "":
                    transcript = 'OK'
                elif response['reason'] == "QUEUED":
                    transcript = 'QUEUED'
                else:
                    transcript = 'FAILURE'

            elif response['result'] == 'ERROR':
                    transcript = 'ERROR_TIME'

            else:
                transcript = 'ERROR'
        except:
            transcript = 'ERROR'

        return transcript
