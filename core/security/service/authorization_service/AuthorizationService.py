import json
import os

from service.authorization_service.IAuthorizationService import IAuthorizationService
from tools.ACNLogger import ACNLogger


class AuthorizationService(IAuthorizationService):
    """Returns formatted JSON with Authorization response information.

    Returns:
        A JSON with Security response information. For example,
        {
            "authorization": { "OK", txt_error }
            "level": [
                {
                    "sap": { "yes", "no" }
                }
            ]
        }

    """
    def __init__(self):
        IAuthorizationService.__init__(self)
        self.logger = ACNLogger(name="AuthorizationService", file="logs/auth-security.log")

    def check_authorization(self, session):
        res = {
            'authorization': 'Lo siento, no está autorizado a acceder a este recurso',
            'level': {
                'sap': 'no'
            }
        }

        try:
            auth_file = './service/data/authorized_users.json'
            auth_file_path = os.path.realpath(auth_file)
            if os.path.isfile(auth_file_path):
                # if user in authorized_users['authorized_users']:
                #     res['authorization'] = 'OK'
                with open(auth_file_path) as f:
                    authorized_users = json.load(f)

                # Recording new json of User/Permissions
                for item in authorized_users['authorized_users']:
                    if session == item['user']:
                        res['authorization'] = 'OK'
                        if item['sap'] == "yes":
                            res['level']['sap'] = item['sap']
                        break
            else:
                self.logger.warning(session, "Authorization - Path to config file missing")

        except:
            self.logger.exception("Exception: Security - check_authorization")
            res['authorization'] = ("Lo siento, en este momento no puedo verificar "
                                    "sus permisos para acceder a este recurso")
            res['level']['sap'] = 'no'

        return res
