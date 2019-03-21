import json
import requests

from service.ComponentsFactory import ComponentsFactory
from service.manager.IDialogManager import IDialogManager
from tools.ACNLogger import ACNLogger


class RepositoryDialogManager(IDialogManager):
    """Handles request to Repository Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="RepositoryDialogManager", file="logs/repository-dialog.log")
        self.req_config = self.req_config.get('WA')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        self.endpoint = 'http://' + url + ':' + port + '/exec_repo'
        self.confidence_manager = ComponentsFactory.get_confidence_manager()

    def get_answer(self, context_result, user_id=None, extra_parameters=None):
        """Returns formatted JSON with Security response.

        Args:
            context_result: context information
            user_id: user id
            extra_parameters: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            Boolean
        """
        answer = self._get_answer(context_result)

        return answer

    def _repo_answer_interpreter(self, context_result, repo_response):
        faq_response = False
        intent_confidence = False
        try:
            if repo_response is not None:
                # Response status
                status = repo_response["status"]
                if status != 200:
                    # Update context
                    context_result.update_answer("Watson Assistant not available!")
                    return True
                elif len(repo_response["entities"]) == 0 and not repo_response["intent"]:
                    # Watson Assistant empty
                    context_result.update_answer("Watson Assistant empty!")
                    return False

                # Get FAQ answer if any
                if len(repo_response["response"]) > 0:
                    faq_response = repo_response["response"][0].strip()

                # Get intent confidence
                intent = repo_response["intent"]
                if intent:
                    intent_confidence = self.confidence_manager.get_answer(
                        nlu_item=intent,
                        confidence_score=repo_response["confidence"],
                        context_result=context_result)

                self.logger.debug(context_result.session, "response: {0}" .format(bool(faq_response and intent_confidence)))

        except:
            self.logger.exception("Exception: Repo - answer_interpreter")
            faq_response = False
            intent_confidence = False

        return bool(faq_response and intent_confidence)

    def _get_answer(self, context_result):
        # Request
        answer = {
            "session": context_result.session,
            "query": context_result.question
        }
        headers = {
            'content-type': "application/json"
        }

        # Response with
        payload = json.dumps(answer)
        response = requests.request("POST", self.endpoint, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(context_result.session, "get_answer - response: {0}".format(response))

        # Update context
        context_result.update_from_repo_response(response)

        return self._repo_answer_interpreter(context_result, response)
