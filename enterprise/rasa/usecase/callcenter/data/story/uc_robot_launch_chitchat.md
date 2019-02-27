## robot + chitchat + alone
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

## robot + chitchat + followup
    - followup{"name": "action_listen"}

## robot + chitchat x inform x inform x inform x inform
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
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - utter_anything_else
    - action_reset_history_and_form

## robot + inform x chitchat x inform x inform x inform
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
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* form: inform{"session": "session", "sys-number": "sys-number"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - form: robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* form: inform{"session": "session", "currency": "currency"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - utter_anything_else
    - action_reset_history_and_form

## robot + inform  x inform x chitchat x inform x inform
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
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* form: inform{"session": "session", "currency": "currency"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* form: inform{"session": "session", "paycon": "paycon"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - utter_anything_else
    - action_reset_history_and_form

## robot + inform x inform x inform x chitchat x inform
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"session": "session"}
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
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - utter_anything_else
    - action_reset_history_and_form

#######################################

## robot + chitchat + alone
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

## robot + chitchat + followup
    - followup{"name": "action_listen"}

## robot + chitchat x inform x inform x inform x inform
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
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - utter_anything_else
    - action_reset_history_and_form

## robot + inform x chitchat x inform x inform x inform
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
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - utter_anything_else
    - action_reset_history_and_form

## robot + inform  x inform x chitchat x inform x inform
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
* form: inform{"session": "session", "currency": "currency"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - utter_anything_else
    - action_reset_history_and_form

## robot + inform x inform x inform x chitchat x inform
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
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - utter_anything_else
    - action_reset_history_and_form
