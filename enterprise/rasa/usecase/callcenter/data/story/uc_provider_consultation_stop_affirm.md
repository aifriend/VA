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
    - slot{"adquira": null}
    - slot{"codigo": null}
    - slot{"proveedor": null}
    - slot{"provider_id": null}
    - slot{"system": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}
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
    - slot{"requested_slot": "system"}
* stop
    - utter_stop
* affirm
    - slot{"adquira": null}
    - slot{"codigo": null}
    - slot{"proveedor": null}
    - slot{"provider_id": null}
    - slot{"system": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_stop_followup

## provider + inform x stop x followup
    - utter_anything_else

