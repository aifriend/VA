from typing import Text, List
from context.Entity import Entity
from context.Intent import Intent

local_twofallback_request = ""

RASA_FALLBACK_THRESHOLD = 0.2


class RasaContext:
    """Class with necessary fields in RASA Rasa Context.

    """

    def __init__(self, session=None, intent_cls=None, entity_cls=None):
        # type: (Text, Intent, List[Entity]) -> RasaContext
        """Inits RasaContext with information

        """
        self.session = session
        self.intent = Intent()
        self.entities = []

        if intent_cls is not None:
            if isinstance(intent_cls, Intent):
                self.intent = intent_cls
            else:
                self.intent = Intent("")
        if entity_cls is not None:
            self.entities.extend(entity_cls)

    @classmethod
    def from_request(cls, request):
        intent_cls = Intent(request["intent"]["name"], request["intent"]["confidence"])
        entity_cls_list = []
        for ent in request["entities"]:
            entity_cls_list.append(Entity(ent["name"], ent["value"], ent["confidence"]))
        return cls(request["session"], intent_cls, entity_cls_list)

    def get_json_state(self):
        return [self.session, self.intent, self.entities]

    @staticmethod
    def _is_float(string: Text) -> bool:
        """Check if a string is an float"""
        try:
            float(string)
            return True
        except ValueError:
            return False

    def process_rest(self):
        self.entities.append(Entity("session", self.session, 1.0))

        global local_twofallback_request

        intent_confidence = 1.0
        if self._is_float(self.intent.confidence):
            intent_confidence = round(self.intent.confidence, 2)

        if self.intent.name.lower() == 'affirm' and \
                local_twofallback_request.intent.confidence <= RASA_FALLBACK_THRESHOLD:
            return local_twofallback_request._get_rasa_request(1.0)
        else:
            rasa_request = self._get_rasa_request(intent_confidence)

        local_twofallback_request = self

        return rasa_request

    def _get_rasa_request(self, confidence):
        request = "/" + self.intent.name.lower() + '@' + str(confidence)
        if self.entities.__len__() > 0:
            request = request + "{"
            for i in range(len(self.entities)):
                if i is not 0:
                    request += ", "
                val = self.entities[i].value
                try:
                    request += "\"" + self.entities[i].name.lower() + "\": \"" + str(val) + "\""
                except:
                    request += "\"" + self.entities[i].name.lower() + "\": \"" + val + "\""
            request += "}"

        return request
