## greetings
* greetings{"session": "session"}
    - slot{"session": "session"}
    - action_greetings

## goodbye
* goodbye{"session": "session"}
    - slot{"session": "session"}
    - action_goodbye

## thanks
* thankyou{"session": "session"}
    - slot{"session": "session"}
    - utter_youarewelcome

## gratitude
* gratitude{"session": "session"}
    - slot{"session": "session"}
    - utter_noworries

## compliment
* compliment{"session": "session"}
    - slot{"session": "session"}
    - utter_compliment

## chitchat
* out_of_scope{"session": "session"}
    - slot{"session": "session"}
    - utter_out_of_scope

## gethelp
* gethelp{"session": "session"}
    - slot{"session": "session"}
    - utter_possibilities
    - utter_gethelp

## human_handoff
* human_handoff{"session": "session"}
    - slot{"session": "session"}
    - utter_action_handoff
    - action_reset_form
    - form{"name": null}
    - slot{"requested_slot": null}
    - slot{"step": "0"}

## informs out of formulary
* inform
    - utter_out_of_scope

## afffirm
* affirm OR deny
    - utter_out_of_scope

## Next step not available
* next_step
    - action_next_step

