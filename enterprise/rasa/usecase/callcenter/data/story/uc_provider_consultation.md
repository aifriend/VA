## provider + happy path
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "cnn": "cnn", "macsystem": "macsystem"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"provider_id": "cnn"}
    - slot{"system": "macsystem"}
    - action_reset_history_and_form

## provider + happy path x followup
    - utter_anything_else
 
## provider + inform x inform
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* form: inform{"cnn": "cnn"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"requested_slot": "system"}
* form: inform{"macsystem": "macsystem"}
    - providerconsultation_form
    - slot{"system": "macsystem"}
    - utter_anything_else
    - action_reset_history_and_form

## provider + happy path x followup
    - utter_anything_else

## provider + happy path
* providerconsultation{"cnn": "cnn", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"provider_id": "cnn"}
    - slot{"requested_slot": "system"}
* form: inform{"macsystem": "macsystem"}
    - providerconsultation_form
    - slot{"system": "macsystem"}
    - utter_anything_else
    - action_reset_history_and_form

## provider + happy path
* providerconsultation{"macsystem": "macsystem", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"system": "macsystem"}
    - slot{"requested_slot": "provider_id"}
* form: inform{"cnn": "cnn"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - utter_anything_else
    - action_reset_history_and_form
