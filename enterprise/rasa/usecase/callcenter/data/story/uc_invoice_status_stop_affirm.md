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
    - slot{"session": null}
    - slot{"reference": null}
    - slot{"status": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_stop_followup

## invoice + stop x followup
    - utter_anything_else
