import json

from watson_assistant.auth_service.IAuthService import IAuthService
from watson_assistant.util.HttpUtils import https_request
from tools.ACNLogger import ACNLogger


class AuthService(IAuthService):
    """
    Handles the JSON request and is interpreted by the Authorization service

    Returns:
        HTTP response with the corresponding answer for the token request
        {
            "id": "Xqtkot2U3r6L1D9mAcjRP3nFoQqqwpjVQDyvT4J3cHcI9WrDUA5yMJuUcqmB3g7b",
            "ttl": 1209600,
            "created": "2018-08-13T12:04:10.839Z",
            "userId": "f7e40d1abdcae9dfa2e547399feebae8"
        }

    Raise:
        HTTP response with error code 500
    """
    def __init__(self):
        IAuthService.__init__(self)
        self.logger = ACNLogger(name="AuthService", file="logs/watson-auth.log")
        self.req_config = self.req_config.get('WA')

    # Obtain the security token
    def get_oauth_token(self, session):
        # Request
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'X-IBM-Client-Id': str(self.req_config.get('app_id')),
            'X-IBM-Client-Secret': str(self.req_config.get('app_key')),
            'X-IBM-Token': str(self.req_config.get('app_token')),
            'Origin': str(self.req_config.get('app_origin')),
        }
        body = {
            'username': str(self.req_config.get('login_user')),
            'password': 'p@ssw0rd'
        }

        # Response
        server = str(self.req_config.get('login_server'))
        url = str(self.req_config.get('login_url'))
        status, reason, response = https_request(server, url, 'POST', json.dumps(body), headers)

        token = ""
        if status == 200:  # Authentication OK
            res = json.loads(response)
            # Get token
            token = res['id']
            self.logger.debug(session, "get_oauth_token - response: {0}".format(res))

        return status, reason, token

