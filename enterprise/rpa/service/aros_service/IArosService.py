import json
import sys
import requests

from config import Config


class IArosService:

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

    def get_oauth_token(self, user_name, password):
        """
        Authentication request
        :param user_name:
        :param password:
        :return: Token for authentication
        """
        raise NotImplementedError()

    def get_robot_info(self, oauth_token, robot_id):
        """
        Robot state
        :param oauth_token:
        :param robot_id:
        :return:
        """
        raise NotImplementedError()

    def execute_robot(self, oauth_token, robot_id, pars):
        """
        Execution result
        :param oauth_token:
        :param robot_id:
        :param pars:
        :return:
        """
        raise NotImplementedError()

    def get_permissions(self, oauth_token, user_id):
        """
        Execution result
        :param oauth_token:
        :param user_id:
        :return:
        """
        raise NotImplementedError()

    def check_robot_permission(self, oauth_token, user_id, robot_id):
        """
        User permissions
        :param oauth_token:
        :param user_id:
        :param robot_id:
        :return:
        """
        raise NotImplementedError()

    def check_robotlist_permission(self, oauth_token, user_id):
        """
        User permissions
        :param oauth_token:
        :param user_id:
        :return:
        """
        raise NotImplementedError()

