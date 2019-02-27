import json

from urllib.parse import urlparse
from service.aros_service.IArosService import IArosService
from service.util.HttpUtils import https_request
from tools.ACNLogger import ACNLogger


class ArosService(IArosService):

    def __init__(self):
        IArosService.__init__(self)
        self.logger = ACNLogger(name="ArosService", file="logs/rpa-aros-service.log")
        self.req_config = self.req_config.get('RPA')

    # Obtener el token de seguridad
    def get_oauth_token(self, username, password):
        # Request
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        body = urlparse({
            'grant_type': 'password',
            'username': username,
            'password': password}
        )

        # Response
        server = str(self.req_config.get('aros_server'))
        url = str(self.req_config.get('aros_url_token'))
        response = https_request(server, url, 'POST', body, headers)

        return response

    # Ejemplo:
    # status, reason, token_resp = get_oauth_token('xxxx@email.com', 'xxxxxx')
    # token = json.loads(token_resp.decode('UTF-8'))['access_token']

    # Consultar la información de un robot
    def get_robot_info(self, oauth_token, robotid):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer %s' % oauth_token
        }
        params = urlparse({})
        server = str(self.req_config.get('aros_server'))
        url = str(self.req_config.get('aros_url_info'))
        return https_request(server, url % robotid, 'GET', params, headers)

    # Ejemplo:
    # get_robot_info(token, 'SGO_RPA123@CPX-MID9YNSWXXX')

    # Lanzar un robot con parámetros
    def execute_robot(self, oauth_token, robotid, pars):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % oauth_token
        }
        quoted_pars = ["\"" + p + "\"" for p in pars]

        params = """\
        {
            'RobotId': '%s',
            'RobotName': '',
            'Machine': '',
            'Client': '',
            'Area': '',
            'Alias': '',
            'Version': '',
            'State': 1,
            'Arguments': '%s'
        }""" % (robotid, " ".join(quoted_pars))

        server = str(self.req_config.get('aros_server'))
        url = str(self.req_config.get('aros_url_exec'))
        return https_request(server, url % robotid, 'PUT', params, headers)

    # Ejemplo:
    # execute_robot(token, 'SGO_RPA123@CPX-MID9YNSWXXX', ['param1=value1', 'param2=value2'])

    # Verificar permisos de chatbot
    def get_permissions(self, oauth_token, userid):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer %s' % oauth_token
        }
        params = urlparse({})
        server = str(self.req_config.get('aros_server'))
        url = str(self.req_config.get('aros_url_info'))
        return https_request(server, url % userid.replace('.', '$'), 'GET', params, headers)

    # Ejemplo:
    # perms = get_permissions(token, 's.gomez.oliver')

    # Verificar permisos para lanzar un robot
    def check_robot_permission(self, oauth_token, userid, robotid):
        authorized = False

        user_perms = self.get_permissions(oauth_token, userid)

        json_array = json.loads(user_perms)
        permission = '1-' + robotid.lower()
        if permission in json_array:
            authorized = True

        return authorized

    # Ejemplo:
    # check_robot_permission(token, 's.gomez.oliver', 'sgo_rpa123@cpx-xxxrwmufspf')

    # Verificar permisos para obtener la lista de robots
    def check_robotlist_permission(self, oauth_token, userid):
        authorized = False

        user_perms = self.get_permissions(oauth_token, userid)

        json_array = json.loads(user_perms)
        permission = '2-'
        if permission in json_array:
            authorized = True

        return authorized

    # Ejemplo:
    # check_robotlist_permission(token, 's.gomez.oliver')
