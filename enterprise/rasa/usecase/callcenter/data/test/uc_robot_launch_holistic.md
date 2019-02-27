## robotlaunch + holistic
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* gratitude{"session": "session"}
    - slot{"session": "session"}
    - utter_noworries
* chitchat{"sys-time": "ahora", "session": "session"}
    - slot{"session": "session"}
    - action_chitchat
    - action_robotlaunch_next_step
* affirm{"session": "session"}
    - slot{"session": "session"}
    - action_robotlaunch_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* chitchat{"sys-time": "ahora", "session": "session"}
    - slot{"session": "session"}
    - action_chitchat
    - action_robotlaunch_next_step
* gethelp{"session": "session"}
    - slot{"session": "session"}
    - utter_gethelp
    - utter_possibilities
* next_step{"session": "session", "sys-time": "ayer"}
    - slot{"session": "session"}
    - action_robotlaunch_next_step
* form: inform{"sys-number": "sys-number"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* compliment
    - utter_compliment
* chitchat
    - action_chitchat
    - action_robotlaunch_next_step
* thankyou{"session": "session"}
    - slot{"session": "session"}
    - utter_youarewelcome
* next_step{"session": "session", "sys-time": "ayer"}
    - slot{"session": "session"}
    - action_robotlaunch_next_step
* form: inform{"currency": "currency"}
    - robotlaunch_form
    - slot{"currency": "currency"}

