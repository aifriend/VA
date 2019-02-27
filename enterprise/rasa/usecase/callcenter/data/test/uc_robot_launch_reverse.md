## robotlaunch + recursive (step by step) - 1
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "orgcompras"}
    - action_robotlaunch_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* robotlaunch{"sys-number": "sys-number", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}   
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "currency"} 
    - action_robotlaunch_next_step 
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* robotlaunch{"currency": "currency", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}  
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "paycondition"} 
    - action_robotlaunch_next_step  
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* robotlaunch{"paycon": "paycon", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - slot{"requested_slot": "paycondition"} 
    - action_reset_history_and_form
    - utter_anything_else
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - action_robotlaunch_next_step
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
    - utter_anything_else

## robotlaunch + recursive (step by step) - 2
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* robotlaunch{"cnn": "cnn", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}    
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* robotlaunch{"sys-number": "sys-number", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}   
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "currency"} 
    - action_robotlaunch_next_step 
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* robotlaunch{"currency": "currency", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}  
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "paycondition"} 
    - action_robotlaunch_next_step  
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* robotlaunch{"paycon": "paycon", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - slot{"requested_slot": "paycondition"} 
    - action_reset_history_and_form
    - utter_anything_else
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - action_robotlaunch_next_step
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
    - utter_anything_else

## robotlaunch + recursive (step by step) - 3
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* robotlaunch{"cnn": "cnn", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}    
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "orgcompras"}
    - action_robotlaunch_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "currency"} 
    - action_robotlaunch_next_step 
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* robotlaunch{"currency": "currency", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}  
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "paycondition"} 
    - action_robotlaunch_next_step  
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* robotlaunch{"paycon": "paycon", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - slot{"requested_slot": "paycondition"} 
    - action_reset_history_and_form
    - utter_anything_else
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - action_robotlaunch_next_step
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
    - utter_anything_else

## robotlaunch + recursive (step by step) - 4
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* robotlaunch{"cnn": "cnn", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}    
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "orgcompras"}
    - action_robotlaunch_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* robotlaunch{"sys-number": "sys-number", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}   
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* robotlaunch{"currency": "currency", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}  
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "paycondition"} 
    - action_robotlaunch_next_step  
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* robotlaunch{"paycon": "paycon", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - slot{"requested_slot": "paycondition"} 
    - action_reset_history_and_form
    - utter_anything_else
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - action_robotlaunch_next_step
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
    - utter_anything_else

## robotlaunch + recursive (step by step) - 5
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* robotlaunch{"cnn": "cnn", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}    
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "orgcompras"}
    - action_robotlaunch_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* robotlaunch{"sys-number": "sys-number", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}   
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "currency"} 
    - action_robotlaunch_next_step 
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "paycondition"} 
    - action_robotlaunch_next_step  
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* robotlaunch{"paycon": "paycon", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - slot{"requested_slot": "paycondition"} 
    - action_reset_history_and_form
    - utter_anything_else
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - action_robotlaunch_next_step
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
    - utter_anything_else

## robotlaunch + recursive (step by step) - 6
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* robotlaunch{"cnn": "cnn", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}    
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "orgcompras"}
    - action_robotlaunch_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* robotlaunch{"sys-number": "sys-number", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}   
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "currency"} 
    - action_robotlaunch_next_step 
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* robotlaunch{"currency": "currency", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}  
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* robotlaunch{"paycon": "paycon", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - slot{"requested_slot": "paycondition"} 
    - action_reset_history_and_form
    - utter_anything_else
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - action_robotlaunch_next_step
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
    - utter_anything_else

## robotlaunch + recursive (step by step) - 7
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* robotlaunch{"cnn": "cnn", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}    
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "orgcompras"}
    - action_robotlaunch_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* robotlaunch{"sys-number": "sys-number", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}   
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "currency"} 
    - action_robotlaunch_next_step 
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* robotlaunch{"currency": "currency", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}  
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "paycondition"} 
    - action_robotlaunch_next_step  
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - action_robotlaunch_next_step
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
    - utter_anything_else

## robotlaunch + recursive (step by step) - 8
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - utter_intro
    - robotlaunch_form
    - form{"name": "robotlaunch_form"}
    - slot{"requested_slot": "robot_id"}
* robotlaunch{"cnn": "cnn", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}    
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "orgcompras"}
    - action_robotlaunch_next_step
* form: inform{"cnn": "cnn", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"robot_id": "cnn"}
    - slot{"requested_slot": "orgcompras"}
* robotlaunch{"sys-number": "sys-number", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}   
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "currency"} 
    - action_robotlaunch_next_step 
* form: inform{"sys-number": "sys-number", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"orgcompras": "sys-number"}
    - slot{"requested_slot": "currency"}
* robotlaunch{"currency": "currency", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}  
* robotlaunch{"proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"requested_slot": "paycondition"} 
    - action_robotlaunch_next_step  
* form: inform{"currency": "currency", "session": "session"}
    - slot{"session": "session"}
    - slot{"robot_id": "cnn"}
    - slot{"orgcompras": "sys-number"}
    - robotlaunch_form
    - slot{"currency": "currency"}
    - slot{"requested_slot": "paycondition"}
* robotlaunch{"paycon": "paycon", "proveedor": "proveedor", "organizacion": "organizacion", "codigo": "CIF", "session": "session"}
    - slot{"codigo": "CIF"}
    - slot{"organizacion": "organizacion"}
    - slot{"proveedor": "proveedor"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - slot{"requested_slot": "paycondition"} 
    - action_reset_history_and_form
    - utter_anything_else
* form: inform{"paycon": "paycon", "session": "session"}
    - slot{"session": "session"}
    - robotlaunch_form
    - slot{"paycondition": "paycon"}
    - action_reset_history_and_form
    - utter_anything_else
