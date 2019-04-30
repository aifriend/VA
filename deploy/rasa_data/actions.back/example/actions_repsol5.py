from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import json
import config
import requests

from random import randint
from usecase.callcenter.dialog_manager.BusinessDialogManager import BusinessDialogManager
from usecase.callcenter.dialog_manager.entity.RpaRequest import RasaRpaRequest
from usecase.callcenter.dialog_manager.entity.SapRequest import SapRequest
from usecase.callcenter.nlg.utters import Utters
from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.events import AllSlotsReset
from rasa_core_sdk.forms import FormAction
from typing import Text, List
from tools.ACNLogger import ACNLogger

logger = ACNLogger(name="Rasa", file="../logs/RasaCore.log")
answers = Utters()


def pickutter(utter_arr):
    rand = randint(0, len(utter_arr) - 1)
    return utter_arr[rand]


def replace_u(text, a, b):
    try:
        text = text.replace(a, b)
    except:
        try:
            text = text.decode("utf8").replace(a, b)
        except:
            text = text.decode("utf8").replace(a, b.decode("utf8"))
    return text


def build_answer(session, userID, phone, intent, question, next, grammar):
    if not userID:
        userID = ""

    answer = {
      "answer": {
          "next": next,
          "question": question,
      }
    }

    return json.dumps(answer)


def send_logs(session, action):
    ip_bc = "business-controller"

    url = "http://{}/logs_to_db/{}/{}".format(ip_bc, session, action)
    headers = {
        "session": session
    }
    response = requests.request("GET", url, headers=headers)

    return response.text


class ActionGreet(Action):
    def name(self):
        return "utter_greet_action"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: utter_greet_action")

        message = pickutter(answers.utter_greet_action)
        answer = build_answer(session, "", "", intent, [message], "", "")
        dispatcher.utter_message(answer)

        return [AllSlotsReset()]


class ActionGratitude(Action):
    def name(self):
        return "utter_gratitude_action"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: utter_gratitude_action")

        message = pickutter(answers.utter_gratitude_action)
        answer = build_answer(session, "", "", intent, [message], "", "")
        dispatcher.utter_message(answer)

        return [AllSlotsReset()]


class askForReference(Action):
    def name(self):
        return "utter_ask_for_reference"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: utter_ask_for_reference")

        message = pickutter(answers.utter_ask_for_reference)
        answer = build_answer(session, "", "", intent, [message], "", "")
        dispatcher.utter_message(answer)

        return ""


class farewell(Action):

    def name(self):
        return "utter_goodbye"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: utter_goodbye")
        message = pickutter(answers.utter_goodbye)

        answer = build_answer(session, "", "", intent, [message], "", "")
        dispatcher.utter_message(answer)

        return [AllSlotsReset()]


class cifIgnorance(Action):

    def name(self):
        return "utter_mandatory_field"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: utter_mandatory_field")
        message = pickutter(answers.utter_mandatory_field)

        answer = build_answer(session, "", "", intent, [message], "", "")
        dispatcher.utter_message(answer)

        return ""


class systemIgnorance(Action):

    def name(self):
        return "utter_try_with_ep2"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        cif = tracker.get_slot("cif")
        system = "EP2"
        logger.info(session, "Executing action: utter_try_with_ep2")

        message = pickutter(answers.utter_provider_information_OTHER)
        messageWithcif = replace_u(json.dumps(message), "{cif}", cif)
        message_completed = replace_u(messageWithcif, "{system}", system)

        answer = build_answer(session, "", "", intent, [json.loads(message_completed)], "", "")
        dispatcher.utter_message(answer)

        return [AllSlotsReset()]


class referenceIgnorance(Action):

    def name(self):
        return "utter_mandatory_reference"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: utter_mandatory_reference")

        message = pickutter(answers.utter_mandatory_reference)

        answer = build_answer(session, "", "", intent, [message], "", "")
        dispatcher.utter_message(answer)

        return ""


class ActionNone(Action):
    def name(self):
        return "utter_not_understand"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: utter_not_understand")

        # habrá que probar llamar al webservice/Rpa pasandole ep2
        # try :
        # except:
        message = pickutter(answers.utter_not_understand)

        answer = build_answer(session, "", "", intent, [message], "", "")
        dispatcher.utter_message(answer)

        return ""


class asumeA060(Action):
    def name(self):
        return "asume_a060"

    def run(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        crednif = tracker.get_slot("crednif")
        iscreditor = tracker.get_slot("iscreditor")
        organization = tracker.get_slot("organization")
        currency = tracker.get_slot("builtin.currency")
        paycondition = "A060"
        logger.info(session, "Executing action: asumeA060")

        ROBOT_NAME = "DEATH_R000484",

        if config.DEBUG:
            message = pickutter(answers.utter_robot_launched)
            answer = build_answer(session, "", "", intent, [message], "", "")
            dispatcher.utter_message(answer)
        else:
            if iscreditor == "True":
                rpa_instance = RasaRpaRequest(user_name=session, robot_name=ROBOT_NAME, creditor=crednif, nif=None,
                                              buy_org=organization, currency=currency, pay_cond=paycondition)
            else:
                rpa_instance = RasaRpaRequest(user_name=session, robot_name=ROBOT_NAME, creditor=None, nif=crednif,
                                              buy_org=organization, currency=currency, pay_cond=paycondition)

            # call to the backend
            message = BusinessDialogManager().get_answer("rpa", session, rpa_instance)

            answer = build_rpa_answer(session, "", "", intent, message, "", "")
            dispatcher.utter_message(answer)

        return [AllSlotsReset()]


class utterInvoiceStatus(FormAction):
    RANDOMIZE = False

    def name(self):
        return 'utter_invoice_status'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["reference"]

    def submit(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        reference = tracker.get_slot("reference")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: utter_invoice_status")

        if config.DEBUG:
            if reference == "12345678":

                message = pickutter(answers.utter_invoice_status)
                messageWithReference = replace_u(json.dumps(message), "{reference}", reference)
            elif reference == "09876543":
                message = pickutter(answers.utter_invoice_status_authorization)
                messageWithReference = replace_u(json.dumps(message), "{reference}", reference)

            elif reference == "55555555":
                message = pickutter(answers.utter_invoice_status_recorded)
                messageWithReference = replace_u(json.dumps(message), "{reference}", reference)

            elif reference == "11111111":
                message = pickutter(answers.utter_invoice_status_deleted)
                messageWithReference = replace_u(json.dumps(message), "{reference}", reference)

            else:
                message = pickutter(answers.utter_invoice_status_not_registered)
                messageWithReference = replace_u(json.dumps(message), "{reference}", reference)

            try:
                answer = build_answer(session, "", "", intent, [json.loads(messageWithReference)], "", "")
            except:
                answer = build_answer(session, "", "", intent, [json.loads(json.dumps(messageWithReference))], "", "")
            dispatcher.utter_message(answer)
        else:
            INVOICE_STATUS_ACTION = "Z_XSRM_ESTADO_CUALQUIER_DOC",

            sap_instance = SapRequest(user_name=session, action_name=INVOICE_STATUS_ACTION,
                                       cif=None, system=None, reference=reference)

            # call to the backend
            message = BusinessDialogManager().get_answer("sap", session, sap_instance)

            answer = build_sap_answer(session, "", "", intent, [message], "", "")
            dispatcher.utter_message(answer)

        return [AllSlotsReset()]


class providerInformation(FormAction):
    RANDOMIZE = False

    def name(self):
        return 'utter_provider_information'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["cif", "system"]

    def submit(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")
        cif = tracker.get_slot("cif")
        system = tracker.get_slot("system")
        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: provider_information")

        if config.DEBUG:
            if system == "SRM":

                message = pickutter(answers.utter_provider_information_SRM)
                messageWithcif = replace_u(json.dumps(message), "{cif}", cif)
                message_completed = replace_u(messageWithcif, "{system}", system)
            else:
                message = pickutter(answers.utter_provider_information_OTHER)
                messageWithcif = replace_u(json.dumps(message), "{cif}", cif)
                message_completed = replace_u(messageWithcif, "{system}", system)

            try:
                answer = build_answer(session, "", "", intent, [json.loads(message_completed)], "", "")
            except:
                answer = build_answer(session, "", "", intent, [message_completed], "", "")
            dispatcher.utter_message(answer)
        else:
            PROVIDER_CONSULTATION_ACTION = "Z_XSRM_CONFIGURADO_ADQUIRA"

            sap_instance = SapRequest(user_name=session, action_name=PROVIDER_CONSULTATION_ACTION, cif=cif,
                                       system=system, reference=None)

            # call to the backend
            message = BusinessDialogManager().get_answer("sap", session, sap_instance)

            answer = build_sap_answer(session, "", "", intent, [message], "", "")
            dispatcher.utter_message(answer)

        return [AllSlotsReset()]


class robotLaunch(FormAction):
    RANDOMIZE = False

    def name(self):
        return 'utter_robot_launched'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["crednif", "iscreditor", "organization", "builtin.currency", "paycondition"]

    def submit(self, dispatcher, tracker, domain):
        session = tracker.get_slot("session")

        intent = tracker.latest_message.intent.get("name")
        logger.info(session, "Executing action: robot_launch")

        if config.DEBUG:
            message = pickutter(answers.utter_robot_launched)
            answer = build_answer(session, "", "", intent, [message], "", "")
            dispatcher.utter_message(answer)
        else:
            crednif = tracker.get_slot("crednif")
            iscreditor = tracker.get_slot("iscreditor")
            organization = tracker.get_slot("organization")
            currency = tracker.get_slot("builtin.currency")
            paycondition = tracker.get_slot("paycondition")

            ROBOT_NAME = "DEATH_R000484",

            if iscreditor == "True":
                rpa_instance = RasaRpaRequest(user_name=session, robot_name=ROBOT_NAME, creditor=crednif, nif=None,
                                              buy_org=organization, currency=currency, pay_cond=paycondition)
            else:
                rpa_instance = RasaRpaRequest(user_name=session, robot_name=ROBOT_NAME, creditor=None, nif=crednif,
                                              buy_org=organization, currency=currency, pay_cond=paycondition)

                # call to the backend
                message = BusinessDialogManager().get_answer("rpa", session, rpa_instance)
                answer = build_rpa_answer(session, "", "", intent, message, "", "")
                dispatcher.utter_message(answer)

        return [AllSlotsReset()]


class ActionTransferAgent(Action):
    def name(self):
        return 'action_transfer_agent'

    def run(self, dispatcher, tracker, domain):

        session = tracker.get_slot("session")
        origin = tracker.get_slot("origin")
        intent = tracker.latest_message.intent.get("name")

        logger.info(session, "Executing action: action_transfer_agent")
        logger.info(session, "INTENT".format(intent))

        responseID = ""
        payload = {}

        if origin == "phone":
            answer = "De acuerdo, transfiero la llamada a un agente, ¡hasta pronto!"
            phone = "+34900494406"
        else:
            answer = "Claro, puedes ponerte en contacto a través del teléfono 900494406, yo me ocupo de enviar nuestra conversación para que conozcan el motivo de la llamada"
            phone = "900494406"

        data = {"phoneNumber": phone}

        req = send_logs(session, "Gestion")
        logs = json.loads(req)["logs_sent"]

        logger.info(session, "Response Manager response: " + answer)
        logger.info("logs sent", str(logs))
        answer = build_answer(session, "", intent, answer, data, "handover", [])

        dispatcher.utter_message(answer)

        return []


class ActionCardDuplicate(Action):
    def name(self):
        return 'action_card_duplicate'

    def run(self, dispatcher, tracker, domain):

        session = tracker.get_slot("session")
        phone_id = tracker.get_slot("phoneId")
        origin = tracker.get_slot("origin")
        intent = tracker.latest_message.intent.get("name")

        logger.info(session, "Executing action: action_transfer_agent")
        logger.info(session, "INTENT".format(intent))

        responseID = ""
        payload = {}

        if origin == "phone":
            answer = "De acuerdo, transfiero la llamada a un agente, ¡hasta pronto!"
            phone = "+34900494406"
        else:
            answer = "Claro, puedes ponerte en contacto a través del teléfono 900494406, yo me ocupo de enviar nuestra conversación para que conozcan el motivo de la llamada"
            phone = "900494406"

        data = {"phoneNumber": phone}

        req = send_logs(session, "Duplicado")
        logs = json.loads(req)["logs_sent"]

        logger.info(session, "Response Manager response: " + answer)
        logger.info("logs sent", str(logs))
        answer = build_answer(session, "", intent, answer, data, "handover", [])

        dispatcher.utter_message(answer)

        return []


class ActionJoke(Action):
    def name(self):
        # define the name of the action which can then be included in training stories
        return "action_joke"

    def run(self, dispatcher, tracker, domain):
        # what your action should do
        request = json.loads(requests.get('https://api.chucknorris.io/jokes/random').text) #make an apie call
        joke = request['value'] #extract a joke from returned json response
        dispatcher.utter_message(joke) #send the message back to the user
        return []
