## provider + chitchat^2 + stop
* providerconsultation{"proveedor": "proveedor", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
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
* stop
    - utter_stop
* deny
    - utter_anything_else

## provider + chitchat^2 + stop x inform x inform + followup
    - followup{"name": "action_listen"}

## provider + inform x chitchat^2 + stop x inform
* providerconsultation{"codigo": "CIF", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* form: inform{"cnn": "cnn"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
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
* stop
    - utter_stop
* deny
    - utter_anything_else

## provider + inform x chitchat^2 + stop x inform x followup
    - followup{"name": "action_listen"}
