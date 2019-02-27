## provider + happy path + human_handoff
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "cnn":"cnn", "macsystem": "macsystem"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"provider_id": "cnn"}
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form
 
## provider + inform x inform + human_handoff
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
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form

## provider + inform x inform + human_handoff
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
* form: inform{"macsystem": "macsystem"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form

