## robotlaunch + chitchat + deny
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
* next_step
    - action_robotlaunch_next_step
 
## robotlaunch + chitchat + deny + reset
    - utter_anything_else

## robotlaunch + chitchat + deny x inform x inform x inform x inform
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
* next_step
    - action_robotlaunch_next_step

## robotlaunch + chitchat + deny x inform x inform x inform x inform + followup
    - utter_anything_else

## robotlaunch + inform x chitchat + deny x inform x inform x inform
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
* next_step
    - action_robotlaunch_next_step

## robotlaunch + inform x chitchat + deny x inform x inform x inform + followup
    - utter_anything_else

## robotlaunch + inform x chitchat + deny x inform x inform x inform
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
* next_step
    - action_robotlaunch_next_step

## robotlaunch + inform x chitchat + deny x inform x inform x inform + followup
    - utter_anything_else

## robotlaunch + inform  x inform x chitchat + deny x inform x inform
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
* next_step
    - action_robotlaunch_next_step

## robotlaunch + inform  x inform x chitchat + deny x inform x inform + followup
    - utter_anything_else

## robotlaunch + inform  x inform x chitchat + deny x inform x inform
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
* next_step
    - action_robotlaunch_next_step

## robotlaunch + inform  x inform x chitchat + deny x inform x inform + followup
    - utter_anything_else

## robotlaunch + inform x inform x inform x chitchat + deny x inform
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
* next_step
    - action_robotlaunch_next_step

## robotlaunch + inform x inform x inform x chitchat + deny x inform + followup
    - utter_anything_else

## robotlaunch + inform x inform x inform x chitchat + deny x inform
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
* next_step
    - action_robotlaunch_next_step

## robotlaunch + inform x inform x inform x chitchat + deny x inform + followup
    - utter_anything_else

