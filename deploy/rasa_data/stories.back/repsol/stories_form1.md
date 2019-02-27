## greet
* greet
    - utter_greet

## happy
* thankyou
    - utter_youarewelcome

## goodbye
* goodbye
    - utter_goodbye

## venue_search
* search_venues
    - action_search_venues
    - slot{"venues": [{"name": "Big Arena", "reviews": 4.5}]}

## concert_search
* search_concerts
    - action_search_concerts
    - slot{"concerts": [{"artist": "Foo Fighters", "reviews": 4.5}]}

## compare_reviews_venues
* compare_reviews
    - action_show_venue_reviews

## compare_reviews_concerts
* compare_reviews
    - action_show_concert_reviews

############################################## Get the invoice status

## happy path
* invoicestatus
    - invoicestatus_form
    - form{"name": "invoicestatus_form"}
    - form{"name": null}
    - utter_invoice_slots_values

## request invoice number
* invoicestatus
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

##############################################

## revert gratitude
* gratitude 
    - utter_noworries

## say goodbye
* goodbye
    - utter_goodbye 