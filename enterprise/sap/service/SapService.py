import json
import sys
import requests
import zeep

from config import Config
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport


class SapService:

    def __init__(self):
        req_config = self._get_module_config()
        if len(req_config) > 0:
            self.req_config = req_config.get('SAP_DEV')
        self.user = self.req_config.get('user')
        self.password = self.req_config.get('password')
        self.wsdl = self.req_config.get('wsdl')

    def _parse_doc_answer(self, response):
        result = "NOK"
        try:
            if isinstance(response, str):
                result = "OK"
                transcript = response

            elif response == 'ERROR':
                transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo más tarde."
                              "En caso de persistir el error contacto con ISI_SOPORTE.")

            else:
                transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                              "En caso de persistir el error contacto con ISI_SOPORTE.")

        except:
            transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                          "En caso de persistir el error contacto con ISI_SOPORTE")

        message = {
            "result": result,
            "response": transcript
        }

        return message

    def _parse_adquira_answer(self, response):
        result = "NOK"
        try:
            if isinstance(response, str):
                if response.split('\t')[0] == "OBJID" or response.split('\t')[0] == "BUKR":
                    result = "OK"
                    transcript = "El proveedor está configurado para los siguientes casos: " + str(
                        response)
                else:
                    result = "OK"
                    transcript = response

            elif response == 'ERROR':
                transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo más tarde."
                              "En caso de persistir el error contacto con ISI_SOPORTE.")

            else:
                transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                              "En caso de persistir el error contacto con ISI_SOPORTE.")

        except:
            transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                          "En caso de persistir el error contacto con ISI_SOPORTE")

        message = {
            "result": result,
            "response": transcript
        }

        return message

    def _parse_rpa_answer(self, response):
        result = "NOK"
        try:
            if isinstance(response, str):
                result = "OK"
                transcript = response

            elif response == 'ERROR':
                transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo más tarde."
                              "En caso de persistir el error contacto con ISI_SOPORTE.")

            else:
                transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                              "En caso de persistir el error contacto con ISI_SOPORTE.")

        except:
            transcript = ("No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos."
                          "En caso de persistir el error contacto con ISI_SOPORTE")

        message = {
            "result": result,
            "response": transcript
        }

        return message

    def call_service(self, service):
        res = {'result': 'ERROR', 'response': 'Faltan parametros para procesar la llamada'}

        action_type = service["action"]
        params = service["params"]
        try:
            if action_type == self.req_config.get('invoice_status_action'):
                if 'PI_USUARIO' in params and 'PI_DOCUMENTO' in params:
                    res = self._state_doc(params['PI_USUARIO'], params['PI_DOCUMENTO'])
                    res = self._parse_doc_answer(res)
            elif action_type == self.req_config.get('provider_consultation_action'):
                if 'PI_USUARIO' in params and 'PI_NIF' in params and 'PI_SISTEMA' in params:
                    res = self._config_adquira(params['PI_USUARIO'], params['PI_NIF'], params['PI_SISTEMA'])
                    res = self._parse_adquira_answer(res)
            elif action_type == self.req_config.get('robot_launch_action'):
                if 'PI_CONDICION' in params and'PI_MONEDA' in params and 'PI_NIF' in params and 'PI_ORGANIZACION' in params and 'PI_PROVEEDOR' in params and 'PI_USUARIO' in params:
                    res = self._dummy_sap_rpa(params['PI_CONDICION'], params['PI_MONEDA'], params['PI_NIF'], params['PI_ORGANIZACION'], params['PI_PROVEEDOR'], params['PI_USUARIO'])
                    res = self._parse_rpa_answer(res)
            else:
                res['result'] = "NOK"
                res['response'] = "Tipo de llamada no definida"

        except Exception as exc:
            res['result'] = "NOK"
            res['response'] = str(exc)

        return res

    def _state_doc(self, usuario, documento):
        # Request
        session = Session()
        session.auth = HTTPBasicAuth(self.user, self.password)
        client = zeep.Client(wsdl=self.wsdl, transport=Transport(session=session))

        # Response
        response = client.service.Z_XSRM_ESTADO_CUALQUIER_DOC(PI_USUARIO=usuario, PI_DOCUMENTO=documento)

        return response['PE_MENSAJE']

    def _config_adquira(self, usuario, cnn, sistema):
        # Request
        session = Session()
        session.auth = HTTPBasicAuth(self.user, self.password)
        client = zeep.Client(wsdl=self.wsdl, transport=Transport(session=session))

        # Response
        response = client.service.Z_XSRM_CONFIGURADO_ADQUIRA(PI_USUARIO=usuario, PI_NIF=cnn, PI_SISTEMA=sistema)
        if response['PE_MENSAJE']:
            format_resp = response['PE_MENSAJE']
        else:
            if sistema == "RP2":
                format_resp = self._format_rp2(response)
            else:
                format_resp = self._format_otros(response)

        return format_resp

    def _dummy_sap_rpa(self, condicion, moneda, cnn, organizacion, proveedor, usuario):
        # Request
        session = Session()
        session.auth = HTTPBasicAuth(self.user, self.password)
        client = zeep.Client(wsdl=self.wsdl, transport=Transport(session=session))

        # Response
        response = client.service.Z_XSRM_EXTENDER_PROVEEDOR(PI_CONDICION=condicion, PI_MONEDA=moneda, PI_NIF=cnn, PI_ORGANIZACION=organizacion,  PI_PROVEEDOR=proveedor, PI_USUARIO=usuario)

        return response

    @staticmethod
    def _format_rp2(rawresp: object) -> str:
        fres = "BUKR\tEKOR\tFECH_ENVIO\n"

        for it in rawresp['PE_DATOS_BACKEND'].item:
            fres += it['BUKRS'] + "\t" + it['EKORG'] + "\t" + it['FECH_ENVIO'] + "\n"

        return fres

    @staticmethod
    def _format_otros(rawresp: object) -> str:
        fres = "OBJID\tFECHA\n"

        for it in rawresp['PE_DATOS_SRM'].item:
            fres += it['OBJID'] + "\t" + it['FECHA'] + "\n"

        return fres

    @staticmethod
    def _get_module_config():
        config_endpoint = Config.CONFIG_MODULE_ENDPOINT

        # Request
        headers = {
            'content-type': "application/json"
        }

        # Response
        try:
            config_response = requests.request("GET", config_endpoint, headers=headers)
            config_response.raise_for_status()
            config_response = json.loads(config_response.text)
        except:
            sys.exit('...Run Configuration Service first!')

        return config_response

