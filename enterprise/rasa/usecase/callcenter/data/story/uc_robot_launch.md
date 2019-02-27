## robotlaunch + happy path
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "cnn": "cnn", "currency": "currency", "paycon": "paycon", "sys-number": "sys-number"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - slot{"currency": "currency"}
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form

## robotlaunch + happy path + followup
    - utter_anything_else

## robotlaunch + step by step 
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
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form

## robotlaunch + step by step + followup
    - utter_anything_else

## robotlaunch + step by step 
* robotlaunch{"cnn": "cnn", "session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
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
    - action_reset_history_and_form

## robotlaunch + step by step + followup
    - utter_anything_else

## robotlaunch + step by step 
* robotlaunch{"currency": "currency", "session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"currency": "currency"}
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
    - slot{"requested_slot": "paycondition"}
* form: inform{"session": "session", "paycon": "paycon"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form

## robotlaunch + step by step + followup
    - utter_anything_else

## robotlaunch + step by step 
* robotlaunch{"paycon": "paycon", "session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"paycondition": "paycon"}
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
    - action_reset_history_and_form

## robotlaunch + step by step + followup
    - utter_anything_else

## robotlaunch + step by step 
* robotlaunch{"sys-number": "sys-number", "session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "robot_id"}
* form: inform{"session": "session", "cnn": "cnn"}
    - slot{"session": "session"}
    - form: robotlaunch_form
    - slot{"robot_id": "cnn"}
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
    - action_reset_history_and_form

## robotlaunch + step by step + followup
    - utter_anything_else