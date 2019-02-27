## happy path + human_handoff
* invoicestatus{"session": "session", "pedido": "cesta"}
    - slot{"session": "session"}
    - slot{"pedido": "cesta"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"reference": "1234567890"}
    - slot{"status": "CONFIRMADO"}
    - slot{"reference": null}
    - slot{"status": null}
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form
    
## invoice + step by step + human_handoff
* invoicestatus{"pedido": "factura"}
    - slot{"pedido": "factura"}
    - utter_intro
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* form: inform{"sys-number":"sys-number"}
    - slot{"reference": "sys-number"}
    - form: invoicestatus_form
    - slot{"status": "confirmado"}
* human_handoff{"session": "session"}
    - utter_action_handoff
    - action_reset_history_and_form
