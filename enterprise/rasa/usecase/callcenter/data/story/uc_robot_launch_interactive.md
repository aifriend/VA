## Generated Story -904750279890139786
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - slot{"pedido": null}
    - slot{"adquira": null}
    - slot{"codigo": null}
    - slot{"proveedor": null}
    - slot{"organizacion": null}
    - slot{"robot_id": null}
    - slot{"orgcompras": null}
    - slot{"currency": null}
    - slot{"paycondition": null}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - slot{"session": null}
    - slot{"codigo": null}
    - slot{"organizacion": null}
    - slot{"proveedor": null}
    - slot{"session": null}
    - slot{"robot_id": null}
    - slot{"orgcompras": null}
    - slot{"currency": null}
    - slot{"paycondition": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}

## Generated Story -2510769695067916761
    - form{"name": null}
    - slot{"requested_slot": null}
    - slot{"step": "0"}