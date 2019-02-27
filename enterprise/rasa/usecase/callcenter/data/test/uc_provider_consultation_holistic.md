## provider + holistic
* providerconsultation{"proveedor": "proveedor", "adquira": "Adquira", "session": "session"}
    - slot{"adquira": "Adquira"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - providerconsultation_form
    - form{"name": "providerconsultation_form"}
    - slot{"requested_slot": "provider_id"}
* compliment{"session": "session"}
    - slot{"session": "session"}
    - utter_compliment
* chitchat{"sys-time": "ahora", "session": "session"}
    - slot{"session": "session"}
    - action_chitchat
    - action_providerconsultation_next_step
* next_step{"session": "session"}
    - slot{"session": "session"}
    - action_providerconsultation_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - slot{"requested_slot": "system"}
* chitchat{"sys-time": "ahora", "session": "session"}
    - slot{"session": "session"}
    - action_chitchat
    - action_providerconsultation_next_step
* thankyou{"session": "session"}
    - slot{"session": "session"}
    - utter_youarewelcome
* affirm{"session": "session", "sys-time": "ahora"}
    - slot{"session": "session"}
    - action_providerconsultation_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - providerconsultation_form
    - slot{"provider_id": "cnn"}
    - slot{"requested_slot": "system"}
* form: inform{"macsystem": "macsystem"}
    - slot{"provider_id": "cnn"}
    - form: providerconsultation_form
    - slot{"system": "macsystem"}
    - action_reset_history_and_form