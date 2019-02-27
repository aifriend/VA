## robotlaunch + happy path
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "cnn": "cnn", "currency": "currency", "paycon": "paycon", "sys-number": "sys-number"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - slot{"currency": "currency"}
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form

## robotlaunch + step by step + human_handoff
* robotlaunch{"session": "session", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form

## robotlaunch + happy path + human_handoff
* robotlaunch{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "robot_id"}
* human_handoff
    - utter_action_handoff
    - action_reset_history_and_form

## robotlaunch + step by step + human_handoff
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
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form

## robotlaunch + step by step + human_handoff
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
* human_handoff
    - utter_action_handoff
    - action_reset_history_and_form

## robotlaunch + step by step + human_handoff
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
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form

## robotlaunch + step by step + human_handoff
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
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form

