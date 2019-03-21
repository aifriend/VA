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
    - slot{"reference": null}
    - slot{"status": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_stop_followup

## invoice + chitchat^2 + stop + inform + followup
    - utter_anything_else
