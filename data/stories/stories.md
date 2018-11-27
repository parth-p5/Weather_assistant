## out_of_scope
* out_of_scope
  - utter_sorry_cant_help

## scope_of_work
* scope_of_work
  - utter_what_can_do

## city & affirm path 1
* greet
  - utter_greet
* city{"location": "bangalore"}
  - utter_weather_help
* mood_affirm
  - utter_weather
  - action_get_weather

## city & affirm path
* city{"location": "bangalore"}
  - utter_weather_help
* confirmation.yes
  - utter_weather
  - action_get_weather

## city & affirm path 2
* city{"location": "bangalore"}
  - utter_weather_help
* mood_affirm
  - utter_weather
  - action_get_weather

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

## city & deny path 3
* city{"location": "bangalore"}
  - utter_weather_help
* confirmation.cancel
  - utter_confirmation.cancel

## city & deny path 3
* city{"location": "bangalore"}
  - utter_weather_help
* confirmation.no
  - utter_confirmation.no

## weather path 1
* greet
  - utter_greet
* weather{"location": "bangalore"}
  - utter_weather
  - action_get_weather

## weather path 2
* weather{"location": "banglore"}
  - utter_weather
  - action_get_weather

## weather path 3
* weather{"location": "banglore"}
  - utter_weather
  - action_get_weather

## weather path 4
* weather{"location": "banglore"}
  - utter_weather
  - action_get_weather
* thank
  - utter_thank_reply