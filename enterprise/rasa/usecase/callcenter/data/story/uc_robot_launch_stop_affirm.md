## robot + stop x inform x inform x inform x inform
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* stop
    - utter_stop
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
    - utter_stop_followup

## robot + stop x followup
    - utter_anything_else

## robot + inform x stop x inform x inform x inform
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* form: inform{"session": "session", "cnn": "cnn"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* stop
    - utter_stop
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
    - utter_stop_followup

## robot + stop x followup
    - utter_anything_else

## robot + inform  x inform x stop x inform x inform
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* form: inform{"session": "session", "cnn": "cnn"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* form: inform{"session": "session", "sys-number": "sys-number"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* stop
    - utter_stop
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
    - utter_stop_followup

## robot + stop x followup
    - utter_anything_else

## robot + inform x inform x inform x stop/deny x inform
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* form: inform{"session": "session", "cnn": "cnn"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* form: inform{"session": "session", "sys-number": "sys-number"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* form: inform{"session": "session", "currency": "currency"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* stop
    - utter_stop
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
    - utter_stop_followup

## robot + stop x followup
    - utter_anything_else

