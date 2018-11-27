from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import time
import requests
from config import config

class ActionExample(Action):

    def name(self):
        return "action_get_weather"

    def run(self, dispatcher, tracker, domain):
        
        b = next(tracker.get_latest_entity_values('location'), None)
        print('msg: ', b)

        obj = {
            "bangalore": {
                'lat': 13.006752,
                'long': 77.561737
            },
            "delhi": {
                'lat': 28.629564,
                'long': 77.127724
            },
            "mumbai": {
                'lat': 18.929863,
                'long': 72.833427
            },
            "kolkata": {
                'lat': 22.572645,
                'long': 88.363892
            },
            "chennai": {
                'lat': 13.067439,
                'long': 80.237617
            },
            "pune": {
                'lat': 18.520430,
                'long': 73.856743
            },
            "ahmedabad": {
                'lat': 23.022505,
                'long': 72.571365
            },
            "surat": {
                'lat': 21.170240,
                'long': 72.831062
            },
            "vadodara": {
                'lat': 22.307159,
                'long': 73.181221
            },
            "new york": {
                'lat': 40.712776,
                'long': -74.005974
            }
        }
        
        API_Key = config.API_KEY
        if b == None :
            b = tracker.get_slot('location')

        if b != '' :
            lat = obj[b]['lat']
            lon = obj[b]['long']
            url = 'https://api.darksky.net/forecast/%s/%f,%f?exclude=minutely,hourly,daily,flags' % (API_Key, lat, lon)
            resp = requests.get(url)
            res = resp.json()
            temp = res['currently']['temperature']
            print('F: %f' % temp)
            celsius = round(( (temp - 32) / 1.8 ), 1)
            degree = u"\u00b0"
            dispatcher.utter_message("Temperature is %s%sC." % (celsius, degree))
            dispatcher.utter_message("Looks like it is a %s." % (res['currently']['icon']))
        else :
            dispatcher.utter_message("Sorry, My bad.")
        
        return [SlotSet('location', '')]