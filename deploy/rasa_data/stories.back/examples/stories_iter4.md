## greetings
* greetings
  - utter_greet_action

## gratitude
* gratitude
  - utter_gratitude_action

## did not understand
* None
  - utter_not_understand

## say goodbye
* goodbye
  - utter_goodbye

########################################################### invoice status without reference
* invoicestatus
  - utter_invoice_status
  - slot{"requested_slot" : "reference"}
> utter_ask_for_ref

## ignorance with the reference
> utter_ask_for_ref
* invoicestatus{"reference" : "reference"}
  - utter_invoice_status
  - slot{"reference" : "reference"}

## ignorance with the reference
> utter_ask_for_ref
* no
  - utter_mandatory_reference

########################################################### provider consultation with all information
* providerconsultation
  - utter_provider_information
  - slot{"requested_slot" : "cif"}
> utter_ask_all_info
* providerconsultation{"cif": "cif"}
  - utter_provider_information
  - slot{"cif" : "cif"}
  - slot{"requested_slot" : "system"}
> system_ignore
* providerconsultation{"cif": "cif"}
  - utter_provider_information
  - slot{"system" : "system"}

## provider consultation with any information and ignorance
> utter_ask_all_info
* no
  - utter_mandatory_field

## provider consultation with CIF information
> utter_ask_all_info
* providerconsultation{"CIF": "X12345678"}
  - utter_provider_information
> system_ignore

## provider consultation with any information and ignorance
> system_ignore
* no
  - utter_try_with_ep2

## provider consultation with any information and ignorance  
> system_ignore
* providerconsultation{"system" : "SRM"}
  - utter_provider_information

############################################################# provider extension with all info
* robotlaunch
  - utter_robot_launched
  - slot{"requested_slot" : "crednif"}
* robotlaunch{"crednif" : "crednif"}
  - utter_robot_launched
  - slot{"crednif" : "crednif"}
  - slot{"iscreditor" : "iscreditor"}
  - slot{"requested_slot" : "organization"}
* robotlaunch{"organization" : "organization"}
  - utter_robot_launched
  - slot{"crednif": "crednif"}
  - slot{"iscreditor" : "iscreditor"}
  - slot{"organization" : "organization"}
  - slot{"requested_slot" : "builtin.currency"}
* robotlaunch{"builtin.currency": "builtin.currency"}
  - utter_robot_launched
  - slot{"crednif": "crednif"}
  - slot{"iscreditor" : "iscreditor"}
  - slot{"organization" : "organization"}
  - slot{"builtin.currency" : "builtin.currency"}
  - slot{"requested_slot" : "paycondition"}
> ignore_paycondition

## ignorance when asking for pay condition
> ignore_paycondition
* robotlaunch{"paycondition": "A060"}
  - utter_robot_launched

## ignorance when asking for pay condition
> ignore_paycondition
 * no
   - asume_a060
