## invoice + happy path
* invoicestatus{"pedido": "pedido", "sys-number": "sys-number"}
    - slot{"pedido": "pedido"}
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"reference": "sys-number"}
    - action_reset_history_and_form

## provider + happy path x followup
    - utter_anything_else

## invoice + step by step
* invoicestatus{"session": "session", "pedido": "confirmacion"}
    - slot{"session": "session"}
    - slot{"pedido": "confirmacion"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* form: inform{"sys-number": "sys-number"}
    - slot{"session": "session"}
    - form: invoicestatus_form
    - action_reset_history_and_form

## invoice + step by step + followup
    - utter_anything_else
