import json
from typing import Text
from json import JSONEncoder


class Entity:
    """Class with necessary fields in Entity data.

    """
    def __init__(self, name=None, value=None, confidence=0.0):
        # type: (Text, Text, float) -> None
        self.name = name
        self.value = value
        self.confidence = confidence

    @classmethod
    def from_response(cls, response):
        return cls(response["name"], response["value"], response["confidence"])

    def get_json_state(self):
        return {"name": self.name, "value": self.value, "confidence": self.confidence}


class EntityContextEncoder(JSONEncoder):
    """Class for JSON class serialization.

    """
    def default(self, obj):
        if isinstance(obj, Entity):
            return obj.get_json_state()
        else:
            return json.JSONEncoder.default(self, obj)
