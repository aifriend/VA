import json
import requests

from service.context.RasaContext import RasaContext, RasaContextEncoder
from service.manager.IDialogManager import IDialogManager
from tools.ACNLogger import ACNLogger


class RasaDialogManager(IDialogManager):
    """Handles request to Rasa Core Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="RasaDialogManager", file="logs/rasa-dialog.log")
        self.req_config = self.req_config.get('RASA')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        uri = str(self.req_config.get('uri'))
        self.endpoint = 'http://' + url + ':' + port + '/' + uri

    def get_answer(self, context_result, user_id=None, extra_parameters=None):
        """Returns formatted JSON with repository response.

        Args:
            context_result: object with context information
            user_id: user session information
            extra_parameters: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A JSON with QnAMaker response information. For example:

            {
                "answer": {
                    "session": session,
                    "response": response
                }
            }

        """
        rasa_context = RasaContext.from_context(context_result)

        return self._get_answer(context_result, rasa_context)

    def _get_answer(self, context_result, rasa_context):
        # Request
        headers = {
                    'content-type': "application/json"
                    }
        payload = json.dumps(rasa_context, cls=RasaContextEncoder)
        response = requests.request("POST", self.endpoint, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(context_result.session, "get_answer - response: {0}".format(response))

        # Update context
        context_result.update_from_rasa_response(response)

        return response
