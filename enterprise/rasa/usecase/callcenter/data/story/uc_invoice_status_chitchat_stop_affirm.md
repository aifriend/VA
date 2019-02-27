## invoice + chitchat + stop
* invoicestatus{"session": "session", "pedido": "factura"}
    - slot{"session": "session"}
    - slot{"pedido": "factura"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* chitchat
    - action_chitchat
    - action_invoicestatus_next_step
* stop
    - utter_stop
* affirm
    - action_reset_history_and_form
    - utter_stop_followup

## invoice + chitchat^2 + stop + followup
    - utter_anything_else

## invoice + chitchat^2 + stop + inform
* invoicestatus{"pedido": "confirmacion"}
    - slot{"pedido": "confirmacion"}
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
* stop
    - utter_stop
* affirm
    - action_reset_history_and_form
    - utter_stop_followup

## invoice + chitchat^2 + stop + inform + followup
    - utter_anything_else
