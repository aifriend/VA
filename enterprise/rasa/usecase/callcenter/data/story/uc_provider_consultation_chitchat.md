## provider * chitchat + alone
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step

## provider + chitchat + followup
    - followup{"name": "action_listen"}

## provider * chitchat^2 + alone
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step

## provider + chitchat^2 + followup
    - followup{"name": "action_listen"}

## provider + chitchat + followup
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* inform{"cnn": "cnn"}
    - slot{"requested_slot": "system"}
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"provider_id": "cnn"}
    
## provider + inform x inform
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* form: inform{"cnn": "cnn"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - form: providerconsultation_form
    - slot{"requested_slot": "system"}
    - utter_anything_else
    - action_reset_history_and_form

## provider + inform x inform
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
    - providerconsultation_form
    - form: providerconsultation_form
    - slot{"requested_slot": "system"}
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* form: inform{"macsystem": "macsystem"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - slot{"system": "macsystem"}
    - utter_anything_else
    - action_reset_history_and_form

## provider + chitchat + followup
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
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* form: inform{"macsystem": "macsystem"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - slot{"system": "macsystem"}
    - utter_anything_else
    - action_reset_history_and_form
