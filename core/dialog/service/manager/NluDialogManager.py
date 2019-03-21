import copy
import json
import requests

from urllib.parse import urlencode, quote_plus
from service.ComponentsFactory import ComponentsFactory
from service.manager.IDialogManager import IDialogManager
from service.manager.ConfidenceDialogManager import ConfidenceActionMode


class NluDialogManager(IDialogManager):
    """Handles request to NLU Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.confidence_manager = ComponentsFactory.get_confidence_manager()

    def get_answer(self, context_result, check_confidence=None, extra_parameters=None):
        """Get information about a question using NLU service

        Args:
            context_result: context information
            check_confidence: nlu confidence check (bool)
            extra_parameters: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            Returns object with NLU information
        """
        # check intents and entities confidence and remove if below threshold
        return self._check_confidence(context_result, check_confidence)

    def _check_confidence(self, context_result, check_confidence):
        # Intent confidence filter
        if context_result.intent is not None:
            intent_with_confidence = self._has_intent_confidence(context_result, check_confidence)
            if not intent_with_confidence:
                context_result.intent = None

        # Entity confidence filter
        entity_filtered = copy.copy(context_result.entities)
        for entity in entity_filtered:
            entity_with_confidence = self._has_entity_confidence(entity, context_result, check_confidence)
            if not entity_with_confidence:
                context_result.entities.remove(entity)

    def _has_intent_confidence(self, context, check_confidence):
        return True if check_confidence else self.confidence_manager.get_answer(
            context.intent.name, context.intent.confidence,
            ConfidenceActionMode.INTENT, context)

    def _has_entity_confidence(self, entity, context, check_confidence):
        return True if check_confidence else self.confidence_manager.get_answer(
            entity.name, entity.confidence,
            ConfidenceActionMode.ENTITY, context)

    def _get_luis_answer(self, context_result, check_confidence):
        # Request
        payload = {
            "q": context_result.question
        }
        question = urlencode(payload, quote_via=quote_plus)
        headers = {
            'content-type': "application/json",
            'locale': context_result.locale,
            'session': context_result.session
        }

        # Response
        url = self.endpoint + "/get_answer?{0}".format(question)
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        luis_intent_parameters = json.loads(response.text)

        # Post-processing
        intent = luis_intent_parameters["intent"]
        if intent != "None":
            if self._has_intent_confidence(luis_intent_parameters, check_confidence):
                luis_intent_parameters["intent"] = intent

            # Update context
            context_result.update_from_nlu_response(luis_intent_parameters)

        return context_result
