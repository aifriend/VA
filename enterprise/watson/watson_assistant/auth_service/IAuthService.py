import json
import sys
import requests

from config import Config


class IAuthService:

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

    def get_oauth_token(self, session):
        """
        Authentication token
        :return:
        """
        raise NotImplementedError()
