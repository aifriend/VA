from typing import Text


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

