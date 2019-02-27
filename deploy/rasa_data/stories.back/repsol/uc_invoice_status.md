## Get the invoice status

## happy path
* invoicestatus
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - form{"name": null}
    - utter_invoice_slots_values
* gratitude 
    - utter_noworries
* goodbye
    - utter_goodbye

## request invoice number
* invoicestatus
    - utter_provider_information
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - slot{"requested_slot": "reference"}
* inform
    - slot{"reference": "number"}
    - form: invoicestatus_form
    - slot{"reference": "number"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_invoice_slots_values
* gratitude 
    - utter_noworries
* goodbye
    - utter_goodbye

############################################## 



############################################## REPSOL

## invoice status without reference
* invoicestatus
  - utter_invoicestatus
  - invoicestatus_form
  - slot{"requested_slot" : "reference"}
> utter_ask_for_ref

## ignorance with the reference
> utter_ask_for_ref
* invoicestatus{"reference" : "reference"}
  - invoicestatus_form
  - slot{"reference" : "reference"}

## ignorance with the reference
> utter_ask_for_ref
* no
  - utter_mandatory_reference