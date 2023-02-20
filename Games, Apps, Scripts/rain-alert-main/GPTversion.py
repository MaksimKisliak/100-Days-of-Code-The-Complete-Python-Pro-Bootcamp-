# This code will check if it's raining in your current city every day at 9am and print a message indicating whether it's raining or not.
# This code will use Twilio to send a text message to your personal phone number indicating whether it's raining or not in your current city every day at 9am. You'll need to sign up for a Twilio account and purchase a Twilio phone number to use this code.

import requests
import datetime
from twilio.rest import Client

def check_rain(city, API_key):
    # API endpoint to retrieve weather data for the city
    endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    
    # send a GET request to the endpoint and retrieve the data in JSON format
    response = requests.get(endpoint).json()
    
    # check if it's raining in the city
    if response["weather"][0]["main"] == "Rain":
        return True
    return False

def rain_alert(city, API_key, from_number, to_number, twilio_account_sid, twilio_auth_token):
    # check if it's raining today
    if check_rain(city, API_key):
        message = f"It is raining in {city} today."
    else:
        message = f"No rain today in {city}."
        
    # send the message using Twilio
    client = Client(twilio_account_sid, twilio_auth_token)
    client.messages.create(to=to_number, from_=from_number, body=message)

if __name__ == "__main__":
    # Replace with your own API key
    API_key = "your_api_key_here"
    
    # Replace with your current city
    city = "San Francisco, US"
    
    # Replace with your Twilio account SID and authentication token
    twilio_account_sid = "your_twilio_account_sid_here"
    twilio_auth_token = "your_twilio_auth_token_here"
    
    # Replace with the Twilio phone number that you purchased
    from_number = "your_twilio_number_here"
    
    # Replace with your personal phone number that you want to send the message to
    to_number = "your_personal_number_here"
    
    # schedule the alert to run every day at 9am
    while True:
        now = datetime.datetime.now()
        if now.hour == 9:
            rain_alert(city, API_key, from_number, to_number, twilio_account_sid, twilio_auth_token)
            break
