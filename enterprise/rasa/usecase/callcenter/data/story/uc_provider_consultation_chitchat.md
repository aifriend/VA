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
    - slot{"requested_slot": "system"}
    - utter_anything_else
    - slot{"adquira": null}
    - slot{"codigo": null}
    - slot{"proveedor": null}
    - slot{"provider_id": null}
    - slot{"system": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}

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
    - slot{"adquira": null}
    - slot{"codigo": null}
    - slot{"proveedor": null}
    - slot{"provider_id": null}
    - slot{"system": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}
