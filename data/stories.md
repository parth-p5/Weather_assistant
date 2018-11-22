## out_of_scope
* out_of_scope
  - utter_sorry_cant_help

## scope_of_work
* scope_of_work
  - utter_what_can_do

## happy path               <!-- name of the story - just for debugging -->
* greet              
  - utter_greet
* mood_great               <!-- user utterance, in format _intent[entities] -->
  - utter_happy

## sad path 1               <!-- this is already the start of the next story -->
* greet
  - utter_greet             <!-- action of the bot to execute -->
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## city & affirm path 1
* greet
  - utter_greet
* city{"location": "bangalore"}
  - utter_weather_help
* mood_affirm
  - utter_weather
  - action_example

## city & affirm path 2
* city{"location": "bangalore"}
  - utter_weather_help
* mood_affirm
  - utter_weather
  - action_example

## city & deny path 1
* greet
  - utter_greet
* city{"location": "bangalore"}
  - utter_weather_help
* mood_deny
  - utter_goodbye

## city & deny path 2
* city{"location": "bangalore"}
  - utter_weather_help
* mood_deny
  - utter_goodbye

## weather path 1
* greet
  - utter_greet
* weather{"location": "bangalore"}
  - utter_weather
  - action_example
* goodbye
  - utter_goodbye

## weather path 2
* weather{"location": "banglore"}
  - utter_weather
  - action_example
* goodbye
  - utter_goodbye

## weather path 3
* weather{"location": "banglore"}
  - utter_weather
  - action_example

## weather path 4
* weather{"location": "banglore"}
  - utter_weather
  - action_example
* thank
  - utter_thank_reply

## thanks
* thank
  - utter_thank_reply