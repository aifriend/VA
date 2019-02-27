import json
from typing import Text
from json import JSONEncoder


class Intent:
    """Class with necessary fields in Intent data.

    """
    def __init__(self, intent_name=None, confidence=0.0):
        # type: (Text, float) -> None
        self.name = str(intent_name)
        self.confidence = confidence

    def get_json_state(self):
        return {"name": self.name, "confidence": self.confidence}


class IntentContextEncoder(JSONEncoder):
    """Class for JSON class serialization.

    """
    def default(self, obj):
        if isinstance(obj, Intent):
            return obj.get_json_state()
        else:
            return json.JSONEncoder.default(self, obj)
