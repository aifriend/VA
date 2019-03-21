## robotlaunch + chitchat + stop x inform x inform x inform x inform
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
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

## robotlaunch + chitchat + stop x inform x inform x inform x inform + followup
    - utter_anything_else

## robotlaunch + inform x chitchat + stop x inform x inform x inform
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
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
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

## robotlaunch + inform x chitchat + stop x inform x inform x inform + followup
    - utter_anything_else

## robotlaunch + inform  x inform x chitchat + stop x inform x inform
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
    - slot{"robot_id": "currency"}
    - slot{"requested_slot": "orgcompras"}
* form: inform{"session": "session", "sys-number": "sys-number"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
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

## robotlaunch + inform  x inform x chitchat + stop x inform x inform + followup
    - utter_anything_else

## robotlaunch + inform x inform x inform x chitchat + stop x inform
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
    - slot{"requested_slot": "paycaondition"}
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
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

## robotlaunch + inform x inform x inform x chitchat + stop x inform + followup
    - utter_anything_else
