import requests
import os
import datetime as dt

QUERY = input('Tell me which exercises you did: ')
GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 182
AGE = 26

# Get the API Key and App ID from environment variables
APP_KEY = os.environ.get("APP_KEY")
APP_ID = os.environ.get("APP_ID")

# Get the exercise endpoint from environment variables
EXERCISE_ENDPOINT = os.environ.get('EXERCISE_ENDPOINT')

# Set the headers for the nutritionix API request
nutri_headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'Content-Type': "application/json"
}

# Set the request body for the nutritionix API request
body = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Make a POST request to the nutritionix API and get the response in JSON format
nutritionix_data = requests.post(EXERCISE_ENDPOINT, headers=nutri_headers, json=body).json()

# Get the name, duration, and calories burned from the response
exercise = nutritionix_data['exercises'][0]['name']
duration = nutritionix_data['exercises'][0]['duration_min']
calories = nutritionix_data['exercises'][0]['nf_calories']

# Get the current time and date
time = dt.datetime.now().strftime("%H:%M:%S")
date = dt.datetime.now().strftime("%d/%m/%Y")

# Set the request body for the sheety API request
body_to_sheety = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': exercise.title(),
        'duration': duration,
        'calories': calories
    }
}

# Get the sheety API endpoint and token from environment variables
sheety_endpoint = os.environ.get("SHEET_ENDPOINT")
sheety_token = os.environ.get("TOKEN")

# Set the headers for the sheety API request
sheety_headers = {
    'Authorization': sheety_token,
    'Content-Type': 'application/json'
}

# Make a POST request to the sheety API and print the response text
print(requests.post(sheety_endpoint, headers=sheety_headers, json=body_to_sheety).text)


# Edit rows

# sheety_endpoint_edit = 'https://api.sheety.co/31e0bcf6faef905452c27badb94434d7/myWorkouts/workouts/3' # pick a row at the end of endpoint
#
# body_to_sheety_edit = {'workout': {'date': '16/06/2005',
#                                   'time': '13:12:12'
#                                    }
#                       }
#
# print(requests.put(sheety_endpoint_edit, headers=sheety_headers, json=body_to_sheety_edit).text)
