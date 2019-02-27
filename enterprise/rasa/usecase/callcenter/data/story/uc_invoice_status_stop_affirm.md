## invoice + stop
* invoicestatus{"session": "session", "pedido": "cesta"}
    - slot{"session": "session"}
    - slot{"pedido": "cesta"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* stop
    - utter_stop
* affirm
    - action_reset_history_and_form
    - utter_stop_followup

## invoice + stop x followup
    - utter_anything_else