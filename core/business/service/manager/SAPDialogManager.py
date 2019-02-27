import json
import requests

from service.manager.IDialogManager import IDialogManager
from tools.ACNLogger import ACNLogger


class SAPDialogManager(IDialogManager):
    """Handles request to SAP Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="SAPDialogManager", file="logs/sap-business.log")
        self.req_config = self.req_config.get('SAP_DEV')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        self.endpoint = 'http://' + url + ':' + port + '/sap_ws'

    def get_answer(self, sap_request, session=None, extra_parameters=None):
        """Returns formatted JSON with SAP response.

        Args:
            sap_request: object with RASA information
            session: user session information
            extra_parameters: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A JSON with SAP response information.
            {
                "response": [OK, ERROR],
                "reason": [QUEUED,...]
            }
        """
        answer = self._get_answer(session, sap_request)

        return answer

    def _get_answer(self, session, sap_request):
        # Request
        answer = {
            "action": sap_request['action_name'],
            "params": {}
        }
        answer["params"]["PI_USUARIO"] = sap_request['user_name']
        answer["params"]["PI_CIF"] = sap_request['cnn']
        answer["params"]["PI_SISTEMA"] = sap_request['system']
        answer["params"]["PI_DOCUMENTO"] = sap_request['reference']
        answer["params"]["PI_CONDICION"] = sap_request['pay_cond']
        answer["params"]["PI_MONEDA"] = sap_request['currency']
        answer["params"]["PI_NIF"] = sap_request['cnn']
        answer["params"]["PI_ORGANIZACION"] = sap_request['buy_org']
        answer["params"]["PI_PROVEEDOR"] = sap_request['creditor']
        headers = {
            'content-type': "application/json"
        }

        # Response
        try:
            payload = json.dumps(answer)
            response = requests.request("POST", self.endpoint, data=payload, headers=headers)
            response.raise_for_status()
            answer_dm = json.loads(response.text)

        except:
            answer_dm = {'result': 'ERROR', 'response': "SAP Get answer"}
            self.logger.exception("Exception: {0}".format(answer_dm))

        return answer_dm

