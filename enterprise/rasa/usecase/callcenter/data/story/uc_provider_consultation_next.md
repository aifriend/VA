## provider + next_step
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* next_step
    - action_providerconsultation_next_step

* providerconsultation{"proveedor": "proveedor", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* chitchat
    - action_chitchat
    - action_providerconsultation_next_step
* next_step
    - action_providerconsultation_next_step
    
## provider + next_step x inform x inform + followup
    - utter_anything_else

## provider + inform x next_step x inform
* providerconsultation{"proveedor": "proveedor", "adquira": "Marketplace"}
    - slot{"adquira": "Marketplace"}
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
* next_step
    - action_providerconsultation_next_step

## provider + inform x next_step x inform + followup
    - utter_anything_else

