## invoice + happy path
* invoicestatus{"session": "session", "pedido": "pedido", "sys-number": "sys-number"}
    - slot{"session": "session"}
    - slot{"pedido": "pedido"}
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"reference": "sys-number"}
    - slot{"session": null}
    - slot{"reference": null}
    - slot{"status": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}

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
    - form: invoicestatus_form
    - slot{"session": null}
    - slot{"reference": null}
    - slot{"status": null}
    - slot{"step": "0"}
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}

## invoice + step by step + followup
    - utter_anything_else
