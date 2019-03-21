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
    - slot{"adquira": null}
    - slot{"codigo": null}
    - slot{"proveedor": null}
    - slot{"provider_id": null}
    - slot{"system": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}

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
    - slot{"requested_slot": "system"}
* form: inform{"macsystem": "macsystem"}
    - providerconsultation_form
    - slot{"system": "macsystem"}
    - utter_anything_else
    - slot{"session": null}
    - slot{"adquira": null}
    - slot{"codigo": null}
    - slot{"proveedor": null}
    - slot{"provider_id": null}
    - slot{"system": null}
    - form{"name": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}

## provider + happy path x followup
    - utter_anything_else

