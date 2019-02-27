## provider + recursive (step by step) - 1 - 1
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* providerconsultation{"sys-number": "sys-number", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* form: inform{"provider_id": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* providerconsultation{"macsystem": "macsystem", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else
* form: inform{"macsystem": "macsystem", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else

## provider + recursive (step by step) - 1 - 2
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* providerconsultation{"sys-number": "sys-number", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* form: inform{"provider_id": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"requested_slot": "system"}
    - action_providerconsultation_next_step
* form: inform{"macsystem": "macsystem", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else

## provider + recursive (step by step) - 2 - 1
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - action_providerconsultation_next_step
* form: inform{"provider_id": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* providerconsultation{"macsystem": "macsystem", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else
* form: inform{"macsystem": "macsystem", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else
    
## provider + recursive (step by step) - 2 - 2
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - action_providerconsultation_next_step
* form: inform{"provider_id": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"requested_slot": "system"}
    - action_providerconsultation_next_step
* form: inform{"macsystem": "macsystem", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else

## provider + recursive (step by step) - 3 - 1
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* providerconsultation{"sys-number": "sys-number", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* form: inform{"provider_id": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* providerconsultation{"macsystem": "macsystem", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else
* form: inform{"macsystem": "macsystem", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else

## provider + recursive (step by step) - 3 - 2
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - action_providerconsultation_next_step
* form: inform{"provider_id": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* providerconsultation{"macsystem": "macsystem", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else
* form: inform{"macsystem": "macsystem", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else
 
## provider + recursive (step by step) - 4 - 1
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* providerconsultation{"sys-number": "sys-number", "proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* form: inform{"provider_id": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"requested_slot": "system"}
    - action_providerconsultation_next_step
* form: inform{"macsystem": "macsystem", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else

## provider + recursive (step by step) - 4 - 2
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - action_providerconsultation_next_step
* form: inform{"provider_id": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"provider_id": "sys-number"}
    - slot{"requested_slot": "system"}
* providerconsultation{"proveedor": "proveedor", "codigo": "CIF", "adquira": "Marketplace", "session": "session"}
    - slot{"adquira": "Marketplace"}
    - slot{"codigo": "CIF"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"requested_slot": "system"}
    - action_providerconsultation_next_step
* form: inform{"macsystem": "macsystem", "session": "session"}
    - slot{"session": "session"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form
    - utter_anything_else
