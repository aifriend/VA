import json
import sys
from typing import Dict, Text, Any, List, Union
import requests
from config import Config
from dialog_manager.BusinessDialogManager import BusinessDialogManager
from dialog_manager.entity.RasaSapRequest import RasaSapRequest
from rasa_core_sdk import ActionExecutionRejection, events
from rasa_core_sdk import Tracker
from rasa_core_sdk.events import SlotSet
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction, REQUESTED_SLOT


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


class InvoicestatusForm(FormAction):
    """invoicestatus_form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "invoicestatus_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["reference"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]

        return {
            "reference": [self.from_entity(entity="reference", intent=["inform", "invoicestatus"], not_intent="chitchat")],
            "status": [self.from_entity(entity="status")]
            }

    @staticmethod
    def request_reference_status(session, reference):
        # type: () -> Text
        """Call backend service -> SAP"""

        # request invoice status action
        action = _get_module_config.get('SAP_DEV').get('invoice_status_action')
        sap_instance = RasaSapRequest(
            user_name=session, action_name=action, cif=None, system=None, reference=reference)

        # call to the backend
        message = BusinessDialogManager().get_answer("sap", session, sap_instance)

        return message

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'reference':
                if not self.is_int(value) or int(value) <= 0:
                    dispatcher.utter_template('utter_wrong_reference', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

                session = tracker.get_slot("session")
                reference = value.lower()
                status_response = self.request_reference_status(session, reference)
                slot_values['status'] = status_response

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        message = ""
        invoice_status = tracker.get_slot("status")
        if invoice_status == 'OK':
            message = "El proveedor está configurado para los siguientes casos: \n" + str(invoice_status['response'])
        elif invoice_status == 'QUEUE':
            message = "No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos. " \
                      "En caso de persistir el error contacto con ISI_SOPORTE"
        elif invoice_status == 'FAILURE':
            message = "No ha sido posible tramitar su petición, por favor, inténtelo más tarde. " \
                      "En caso de persistir el error contacto con ISI_SOPORTE"
        elif invoice_status == 'ERROR_TIME':
            message = "No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos. " \
                      "En caso de persistir el error contacto con ISI_SOPORTE"
        elif invoice_status == 'ERROR':
            message = "No ha sido posible tramitar su petición, por favor, inténtelo dentro de unos minutos. " \
                      "En caso de persistir el error contacto con ISI_SOPORTE"
        else:
            dispatcher.utter_template('utter_invoicestatus_status', tracker)

        session = tracker.get_slot("session")
        intent = tracker.latest_message.intent.get("name")
        answer = build_answer(session, "", "", intent, [message], "", "")
        dispatcher.utter_message(answer)

        return [events.AllSlotsReset()]


class RobotlaunchForm(FormAction):
    """robotlaunch_form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "robotlaunch_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["id", "organizacion", "money", "paycon"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to:
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "reference": self.from_entity(entity="cuisine", not_intent="chitchat"),
            "num_people": [self.from_entity(entity="num_people", intent=["inform", "request_restaurant"]), self.from_entity(entity="reference")],
            "outdoor_seating": [self.from_entity(entity="seating"), self.from_intent(intent='affirm', value=True), self.from_intent(intent='deny', value=False)],
            "preferences": [self.from_intent(intent='deny', value="no additional preferences"), self.from_text(not_intent="affirm")],
            "feedback": [self.from_entity(entity="feedback"), self.from_text()]
            }

    @staticmethod
    def request_reference_status(session, reference):
        # type: () -> Text
        """Call backend service -> RPA"""

        # request invoice status action
        action = _get_module_config().get('SAP_DEV').get('invoice_status_action')
        sap_instance = RasaSapRequest(user_name=session, action_name=action, robot_name="robot_name", creditor=reference.crednif,
                                        nif=None, buy_org=reference.organization, currency=reference.currency,
                                        pay_cond=reference.paycondition)
        
        # call to the backend
        message = BusinessDialogManager().get_answer("sap", session, sap_instance)

        return message

    @staticmethod
    def _db():
        # type: () -> List[Text]
        """_"""
        return []

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'cuisine':
                if value.lower() not in self._db():
                    dispatcher.utter_template('utter_wrong_cuisine', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'num_people':
                if not self.is_int(value) or int(value) <= 0:
                    dispatcher.utter_template('utter_wrong_num_people', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'outdoor_seating':
                if isinstance(value, str):
                    if 'out' in value:
                        # convert "out..." to True
                        slot_values[slot] = True
                    elif 'in' in value:
                        # convert "in..." to False
                        slot_values[slot] = False
                    else:
                        dispatcher.utter_template('utter_wrong_outdoor_seating', tracker)
                        # validation failed, set slot to None
                        slot_values[slot] = None

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []


class ProviderconsultationForm(FormAction):
    """providerconsultation_form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "providerconsultation_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["id", "macsystem"]

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to:
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "reference": self.from_entity(entity="cuisine", not_intent="chitchat"),
            "num_people": [self.from_entity(entity="num_people", intent=["inform", "request_restaurant"]), self.from_entity(entity="reference")],
            "outdoor_seating": [self.from_entity(entity="seating"), self.from_intent(intent='affirm', value=True), self.from_intent(intent='deny', value=False)],
            "preferences": [self.from_intent(intent='deny', value="no additional preferences"), self.from_text(not_intent="affirm")],
            "feedback": [self.from_entity(entity="feedback"), self.from_text()]
            }

    @staticmethod
    def request_provider_consultation(session, reference):
        # type: () -> Text
        """Call backend service -> SAP"""

        # request_provider_consultation action
        action = _get_module_config().get('SAP_DEV').get('provider_consultation_action')
        sap_instance = RasaSapRequest(
            user_name=session, action_name=action, cif=None, system=None, reference=reference)

        # call to the backend
        message = BusinessDialogManager().get_answer("sap", session, sap_instance)

        return message

    @staticmethod
    def _db():
        # type: () -> List[Text]
        """_"""
        return []

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate(self,
                 dispatcher: CollectingDispatcher,
                 tracker: Tracker,
                 domain: Dict[Text, Any]) -> List[Dict]:
        """Validate extracted requested slot
            else reject the execution of the form action
        """
        # extract other slots that were not requested
        # but set by corresponding entity
        slot_values = self.extract_other_slots(dispatcher, tracker, domain)

        # extract requested slot
        slot_to_fill = tracker.get_slot(REQUESTED_SLOT)
        if slot_to_fill:
            slot_values.update(self.extract_requested_slot(dispatcher,
                                                           tracker, domain))
            if not slot_values:
                # reject form action execution
                # if some slot was requested but nothing was extracted
                # it will allow other policies to predict another action
                raise ActionExecutionRejection(self.name(),
                                               "Failed to validate slot {0} "
                                               "with action {1}"
                                               "".format(slot_to_fill,
                                                         self.name()))

        # we'll check when validation failed in order
        # to add appropriate utterances
        for slot, value in slot_values.items():
            if slot == 'cuisine':
                if value.lower() not in self._db():
                    dispatcher.utter_template('utter_wrong_cuisine', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'num_people':
                if not self.is_int(value) or int(value) <= 0:
                    dispatcher.utter_template('utter_wrong_num_people', tracker)
                    # validation failed, set slot to None
                    slot_values[slot] = None

            elif slot == 'outdoor_seating':
                if isinstance(value, str):
                    if 'out' in value:
                        # convert "out..." to True
                        slot_values[slot] = True
                    elif 'in' in value:
                        # convert "in..." to False
                        slot_values[slot] = False
                    else:
                        dispatcher.utter_template('utter_wrong_outdoor_seating', tracker)
                        # validation failed, set slot to None
                        slot_values[slot] = None

        # validation succeed, set the slots values to the extracted values
        return [SlotSet(slot, value) for slot, value in slot_values.items()]

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_template('utter_submit', tracker)
        return []
