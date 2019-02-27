## provider + inform + stop
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* stop
    - utter_stop
* affirm
    - action_reset_history_and_form
    - utter_stop_followup

## provider + inform x stop x inform + followup
    - utter_anything_else

## provider + inform x stop x affirm
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* form: inform{"cnn": "cnn"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - form: providerconsultation_form
    - slot{"requested_slot": "system"}
* stop
    - utter_stop
* affirm
    - action_reset_history_and_form
    - utter_stop_followup

## provider + inform x stop x followup
    - utter_anything_else

