import json

from typing import Text
from watson_assistant.util.HttpUtils import https_request
from watson_assistant.wd_service.IWdService import IWdService
from tools.ACNLogger import ACNLogger


class WdService(IWdService):
    """
    Handles the JSON request and is interpreted by the Watson Discovery service

    Request:
    {
        "request": {
            "query": "my request",
        }
    }

    Response:
    {
        "result": {
            "content": [
                "… texto encontrado por discovery …"
            ],
            "intent": intent,
            "confidence": 1.0,
            "entities": [
                {
                    "name": entity_name,
                    "value": entity_value,
                    "confidence": 1.0
                }
            ]
        }
    }

    """
    def __init__(self):
        IWdService.__init__(self)
        self.logger = ACNLogger(name="WdService", file="logs/watson-login.log")
        self.req_config = self.req_config.get('WA')

    def execute_wd(self, token, session, query):
        try:
            return self._get_answer_wd(token, session, query)
        except:
            return 500, {"WA - Exception requesting service"}, None

    @staticmethod
    def _is_float(string: Text) -> bool:
        """Check if a string is an float"""
        try:
            float(string)
            return True
        except ValueError:
            return False

    def _get_answer_wd(self, token, session, query):
        # Request
        headers = {
            # DEVELOPMENT
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'X-IBM-Client-Id': str(self.req_config.get('app_id')),
            'X-IBM-Client-Secret': str(self.req_config.get('app_key')),
            'X-IBM-Token': str(self.req_config.get('app_token')),
            'Origin': str(self.req_config.get('app_origin')),
            'Authorization': token,
        }
        body = {
            "request": {
                "query": query
            }
        }
        server = str(self.req_config.get('query_server'))
        url = str(self.req_config.get('query_url'))
        status, reason, response = https_request(server, url, 'POST', json.dumps(body), headers)

        # Response
        answer = {"response": "", "intent": "", "confidence": -1, "entities": [], "status": status}
        if status == 200:  # Authentication OK
            res = json.loads(response)
            wa_response = res["result"]
            # FAQ
            answer["response"] = wa_response["content"]
            # NLU
            answer["intent"] = wa_response["intent"]
            answer["confidence"] = \
                float(wa_response["confidence"]) if self._is_float(wa_response["confidence"]) else str(1.0)
            for entity in wa_response["entities"]:
                entity['confidence'] = \
                    float(entity["confidence"]) if self._is_float(entity["confidence"]) else str(1.0)
                answer["entities"].append(entity)

        answer["session"] = session

        return status, reason, answer
