import json

from json import JSONEncoder
from service.context.Entity import Entity
from service.context.Intent import Intent


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
            self.intent = intent_cls
        if entity_cls is not None:
            self.entities.extend(entity_cls)

    @classmethod
    def from_context(cls, context):
        return cls(context.session, context.intent, context.entities)

    def get_json_state(self):
        json_intent = self.intent.get_json_state()
        json_entity_list = []
        for ent in self.entities:
            entity_cls = ent.get_json_state()
            json_entity_list.append(entity_cls)
        json_res = {"session": self.session, "intent": json_intent, "entities": json_entity_list}

        return json.dumps(json_res)

    def get_payload(self):
        payload = {
            "session": self.session,
            "intent": self.intent,
            "entities": self.entities,
        }

        return payload

    def logger(self, legend):
        return legend + " - intents {0}".format(self.intent) + "\n" + \
               legend + " - entities {0}".format(self.entities)


class RasaContextEncoder(JSONEncoder):
    """Class for JSON class serialization.

    """
    def default(self, obj):
        if isinstance(obj, RasaContext):
            return obj.get_json_state()
        else:
            return json.JSONEncoder.default(self, obj)
