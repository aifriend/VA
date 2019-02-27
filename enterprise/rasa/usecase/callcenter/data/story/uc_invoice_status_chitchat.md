## invoice * chitchat + alone
* invoicestatus{"pedido": "referencia"}
    - slot{"pedido": "referencia"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step

## invoice * chitchat^2 + alone
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

## invoice * chitchat + alone
* invoicestatus{"pedido": "factura"}
    - slot{"pedido": "factura"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* inform{"sys-number": "98376266"}
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"reference": "98376266"}
    - action_reset_history_and_form

## invoice * chitchat + alone
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
* inform{"sys-number": "sys-number"}
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"reference": "sys-number"}
    - action_reset_history_and_form