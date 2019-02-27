## invoice * chitchat + next_step
* invoicestatus{"pedido": "referencia"}
    - slot{"pedido": "referencia"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* next_step
    - action_invoicestatus_next_step

## invoice * chitchat^2 + next_step
* invoicestatus{"session": "session", "pedido": "contrato"}
    - slot{"session": "session"}
    - slot{"pedido": "contrato"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* next_step
    - action_invoicestatus_next_step

## invoice * chitchat + next_step
* invoicestatus{"pedido": "factura"}
    - slot{"pedido": "factura"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* next_step
    - action_invoicestatus_next_step
* inform{"sys-number": "sys-number"}
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"reference": "sys-number"}
* form: inform{"sys-number": "sys-number"}
    - slot{"session": "session"}
    - form: invoicestatus_form
    - slot{"reference": "sys-number"}
    - action_reset_history_and_form

