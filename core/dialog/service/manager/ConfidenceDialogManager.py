import json
import requests

from enum import Enum
from service.manager.IDialogManager import IDialogManager
from tools.ACNLogger import ACNLogger


class ConfidenceActionMode(Enum):
    INTENT = 1
    ENTITY = 2


class ConfidenceDialogManager(IDialogManager):
    """Handles request to Confidence Manager Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="ConfidenceDialogManager", file="logs/confidence-dialog.log")
        self.req_config = self.req_config.get('CONFIDENCE')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        self.endpoint = 'http://' + url + ':' + port

    def get_answer(self, nlu_item, confidence_score=None, action_mode=ConfidenceActionMode.INTENT, context_result=None):
        """Returns formatted JSON with Confidence response.

        Args:
            nlu_item: NLU item requested
            confidence_score: confidence score
            action_mode: action selector
            context_result: object with context information

        Returns:
            A JSON with Security response information. For example,
            {
                "threshold": {True, False}
            }

        """
        answer = self._get_answer(context_result.session, nlu_item, confidence_score, action_mode)

        return bool(answer["threshold"])

    def _apply_entity_threshold(self, session, entity, confidence_score):
        # Request
        payload = {
            "session": session,
            "confidence": confidence_score,
            "entity": entity
        }
        headers = {
            'content-type': "application/json"
        }

        # Response with
        url = self.endpoint + "/entity_lower_confidence"
        payload = json.dumps(payload)
        response = requests.request("POST", url, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(session, "apply_entity_threshold - response: {0} -> {1}".format(payload, response))

        return response  # Entity or ""

    def _apply_intent_threshold(self, session, intent, confidence_score):
        # Request
        payload = {
            "session": session,
            "confidence": confidence_score,
            "intent": intent
        }
        headers = {
            'content-type': "application/json"
        }

        # Response with
        url = self.endpoint + "/intent_lower_confidence"
        payload = json.dumps(payload)
        response = requests.request("POST", url, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(session, "apply_intent_threshold - response: {0} -> {1}".format(payload, response))

        return response  # Intent or ""

    def _get_answer(self, session, nlu_item, confidence_score, action_mode):
        try:
            if action_mode == ConfidenceActionMode.INTENT:
                response = self._apply_intent_threshold(session, nlu_item, confidence_score)
            elif action_mode == ConfidenceActionMode.ENTITY:
                response = self._apply_entity_threshold(session, nlu_item, confidence_score)
            else:
                response = {"threshold": False, "reason": "No configuration defined (intent? or entity?)"}

        except Exception as exc:
            self.logger.exception("Exception: Confidence - get_answer")
            response = {"threshold": False, "reason": exc}

        return response
