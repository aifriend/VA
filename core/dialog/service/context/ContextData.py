from typing import Text, List
from service.context.Entity import Entity
from service.context.Intent import Intent


class ContextData:
    """Class with necessary fields in context data.

    """

    def __init__(self, session=None, intent_cls=None, entity_cls=None,
                 question=None, answer=None, locale=None, authorization=None, level=None, role=None):
        # type: (Text, Intent, List[Entity], Text, Text, Text, Text, Text, Text) -> None
        """Inits ContextData with information

        """
        self.session = session
        self.question = question
        self.answer = answer
        self.locale = locale
        self.authorization = authorization
        self.authorization_level = level
        self.authorization_flow = role
        self.intent = Intent()
        self.entities = []

        if intent_cls is not None:
            self.intent = intent_cls
        if entity_cls is not None:
            if len(entity_cls) > 1:
                self.entities.extend(entity_cls)
            elif len(entity_cls) == 1:
                self.entities.append(entity_cls)

    def update_from_authorization_security_response(self, response):
        try:
            self.authorization = response["authorization"]
            self.authorization_level = response["level"]
        except:
            pass

    def update_from_flow_security_response(self, response):
        try:
            self.authorization_flow = response
        except:
            pass

    def update_from_rasa_response(self, response):
        try:
            self.answer = response
        except:
            pass

    def update_from_repo_response(self, response):
        try:
            # FAQ service response
            self.answer = [{
                "text": response["response"][0] if len(response["response"]) > 0 else "",
                "recipient_id": response["session"]
            }]

            # NLU service response
            self.intent = Intent(response["intent"], response["confidence"])
            for entity in response["entities"]:
                self.entities.append(Entity.from_response(entity))

        except:
            pass

    def update_from_nlu_response(self, response):
        self.intent = Intent(response["intent"], response["score"])
        for entity in response["entities"]:
            self.entities.append(Entity.from_response(entity))

    def update_answer(self, value):
        self.answer = value

    def logger(self, legend):
        return legend + " - {0}".format(self)

    def has_intent(self):
        return isinstance(self.intent, Intent) \
               and len(self.intent.name) > 0 \
               and not self.intent.name.isspace()

    def has_entities(self):
        return self.entities is not None and len(self.entities) > 0

    def has_response(self):
        boolean = False
        if isinstance(self.answer, list):
            if isinstance(self.answer[0]['text'], str) and len(self.answer[0]['text']) > 0:
                boolean = True

        return boolean
