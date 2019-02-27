import json
import sys
import requests

from config import Config


class IWdService:

    def __init__(self):
        req_config = self._get_module_config()
        if len(req_config) > 0:
            self.req_config = req_config

    @staticmethod
    def _get_module_config():
        config_endpoint = Config.CONFIG_MODULE_ENDPOINT

        # Request
        headers = {
            'content-type': "application/json"
        }

        # Response with
        try:
            config_response = requests.request("GET", config_endpoint, headers=headers)
            config_response.raise_for_status()
            config_response = json.loads(config_response.text)
        except:
            sys.exit('...Run Configuration Service first!')

        return config_response

    def execute_wd(self, token, session, query):
        """
        Web service response
        :param token: str(token for request authentication)
        :param session: Session ID
        :param query: str(Query)
        :return:
        """
        raise NotImplementedError()
