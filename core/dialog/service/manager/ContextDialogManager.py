import copy
import json
import requests

from service.context.Entity import Entity, EntityContextEncoder
from service.context.Intent import Intent
from service.manager.IDialogManager import IDialogManager
from enum import Enum
from tools.ACNLogger import ACNLogger


class ContextActionMode(Enum):
    SEND = 1
    GET = 2
    UPDATE = 3
    RESOLVER = 4
    BACK = 5


class ContextDialogManager(IDialogManager):
    """Handles request to Context Service.
    """

    def __init__(self):
        IDialogManager.__init__(self)
        self.logger = ACNLogger(name="ContextDialogManager", file="logs/context-dialog.log")
        self.req_config = self.req_config.get('CONTEXT')
        url = str(self.req_config.get('url'))
        port = str(self.req_config.get('port'))
        self.endpoint = 'http://' + url + ':' + port

    def get_answer(self, context_result, action_mode=ContextActionMode.SEND, extra_parameters=None):
        """Returns formatted JSON with Context Manager.

        Args:
            context_result: context information
            action_mode: conversation action mode
            extra_parameters: Another optional variable, that has a much
                longer name than the other args, and which does nothing.

        Returns:
            A JSON with Security response information. For example,
            {
                "response":
                {
                    SEND -> {"OK": "OK"}
                    GET -> [{...}]
                },
            }

        """
        answer = self._get_answer(context_result, action_mode, extra_parameters)

        return answer

    def _send_logs(self, context_result):
        # Request
        answer = {
            "session": context_result.session,
            "question": context_result.question,
            "answer": context_result.answer,
            "intent": context_result.intent.name,
            "entities": context_result.entities,
            "locale": context_result.locale,
            "authorization": context_result.authorization,
        }
        headers = {
            'content-type': "application/json"
        }

        # Response with
        url = self.endpoint + "/send_logs"
        payload = json.dumps(answer, cls=EntityContextEncoder)
        response = requests.request("POST", url, data=payload, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(context_result.session, "send_logs - response: {0}".format(response))

        return response

    def _update_logs(self, context_result, extra_parameters):
        # Request
        headers = {
            'content-type': "application/json"
        }

        # Response with
        if extra_parameters is not None:
            url = self.endpoint + "/update_logs/{0}/{1}/{2}" \
                .format(context_result.session, extra_parameters["key"], extra_parameters["value"])
            response = requests.request("POST", url, headers=headers)
            response.raise_for_status()
            response = json.loads(response.text)
        else:
            response = "Nothing to update"

        self.logger.debug(context_result.session, "update_logs - response: {0}".format(response))

        return response

    def _get_answer(self, context_result, action_mode, extra_parameters):
        try:
            if action_mode == ContextActionMode.SEND:
                response = self._send_logs(context_result)
            elif action_mode == ContextActionMode.UPDATE:
                response = self._update_logs(context_result, extra_parameters)
            elif action_mode == ContextActionMode.RESOLVER:
                response = self._context_domain_resolver(context_result)
            elif action_mode == ContextActionMode.BACK:
                response = self._context_history_resolver(context_result, extra_parameters)
            else:
                response = self._get_back_logs(context_result)

        except Exception as exc:
            self.logger.exception("Exception: Context - get_answer")
            return {"NOK": "NOK"}

        return response

    def _get_back_logs(self, context_result, back_track=0):
        # Request
        headers = {
            'content-type': "application/json"
        }

        # Response with
        url = self.endpoint + "/get_back_logs/{0}/{1}".format(context_result.session, back_track)
        response = requests.request("GET", url, headers=headers)
        response.raise_for_status()
        response = json.loads(response.text)
        self.logger.debug(context_result.session, "get_back_logs - response: {0}".format(response))

        return response

    def _context_domain_resolver(self, context_result):
        # ENTITIES

        # Entity INFORM replace
        if context_result.has_intent() or context_result.has_entities() or context_result.has_response():
            intent_inform = False
            if len(context_result.entities) > 0:
                intent_inform = self._entity_inform_context_resolver(context_result)

            # Entity filtering
            self._entity_filter(context_result)

            # INTENT

            # Intent NAME replace
            if self._intent_name_context_resolver(context_result):
                return context_result

            # Intent's replacement
            if context_result.has_intent():
                if not intent_inform:
                    # Intent DENY replace
                    intent_deny = self._intent_deny_context_resolver(context_result)
                    if not intent_deny:
                        # Intent CHITCHAT replace
                        _ = self._intent_chitchat_context_resolver(context_result)
        else:
            if not context_result.has_intent():
                context_result.intent = Intent(confidence=1.0)
            context_result.intent.name = "out_of_scope"
        return context_result

    def _context_history_resolver(self, context_result, history_back=-1):
        # back_track = 1  # last history item with or without intent
        # back_track = -1  # last available history item with intent
        back_track = history_back if history_back is not None else -1
        history_item = self._get_back_logs(context_result, back_track=back_track)

        return history_item

    @staticmethod
    def _entity_filter(context_result):
        entity_filtered = copy.copy(context_result.entities)
        for entity in entity_filtered:
            if entity.name == "sys-number" and not str.isdigit(entity.value):
                context_result.entities.remove(entity)
            elif entity.name == "sys-date":
                context_result.entities.remove(entity)
            elif entity.name == "currency":
                entity.value = entity.value.upper()

    @staticmethod
    def _entity_inform_context_resolver(context_result):
        if context_result.intent.name != "invoicestatus" and \
                context_result.intent.name != "robotlaunch" and \
                context_result.intent.name != "providerconsultation":
            for entity in context_result.entities:
                if entity.name == "cnn" or entity.name == "paycon" or entity.name == "macsystem" or \
                        entity.name == "currency" or (entity.name == "sys-number" and str.isdigit(entity.value)):
                    context_result.intent = Intent("inform", entity.confidence)
                    return True

        return False

    @staticmethod
    def _intent_deny_context_resolver(context_result):
        if context_result.intent.name == "isnthappy":
            context_result.intent = Intent("deny", context_result.intent.confidence)
            return True

        return False

    @staticmethod
    def _intent_name_context_resolver(context_result):
        for entity in context_result.entities:
            if entity.name == "person":
                context_result.intent = Intent("greetings", entity.confidence)
                return True

        if context_result.intent.name == "name":
            context_result.intent = Intent("greetings", context_result.intent.confidence)
            return True

        return False

    @staticmethod
    def _intent_chitchat_context_resolver(context_result):
        if context_result.intent.name in ['askcreator', 'askfeeling', 'askjoke', 'getnews',
                                          'getweather', 'insult', 'laught', 'wantdrink',
                                          'ask_howold', 'ask_isbot', 'ask_restaurant',
                                          'ask_wherefrom', 'ishappy', 'ask_howbuilt',
                                          'ask_languagesbot', 'ask_howdoing', 'ask_whatspossible',
                                          'ask_whoisit', 'ask_whoami', 'gettime']:
            # Add internal chitchat intent
            context_result.intent = Intent("chitchat", context_result.intent.confidence)

            return True

        return False
