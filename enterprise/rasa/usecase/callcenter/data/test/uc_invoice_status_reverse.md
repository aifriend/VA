## invoice + recursive (step by step)
* invoicestatus{"pedido": "pedido", "session": "session"}
    - slot{"pedido": "pedido"}
    - slot{"session": "session"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* invoicestatus{"sys-number": "sys-number", "pedido": "pedido", "session": "session"}
    - slot{"pedido": "pedido"}
    - slot{"session": "session"}
    - invoicestatus_form
    - slot{"reference": "sys-number"}
    - action_reset_history_and_form
    - utter_anything_else
* form: invoicestatus{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - invoicestatus_form
    - slot{"reference": "sys-number"}
    - action_reset_history_and_form
    - utter_anything_else
    
## invoice + recursive (step by step)
* invoicestatus{"pedido": "pedido", "session": "session"}
    - slot{"pedido": "pedido"}
    - slot{"session": "session"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* invoicestatus{"pedido": "pedido", "session": "session"}
    - slot{"pedido": "pedido"}
    - slot{"session": "session"}
    - invoicestatus_form
    - slot{"requested_slot": "reference"}
    - action_invoicestatus_next_step
* form: invoicestatus{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - invoicestatus_form
    - slot{"reference": "sys-number"}
    - action_reset_history_and_form
    - utter_anything_else
    