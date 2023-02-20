# # This code uses the requests library to make two API requests: one to the Nutritionix API to retrieve the exercise information, and one to the Sheety API to send the data to a Google Sheets spreadsheet. The payload for the Sheety API request includes the exercise name, duration, calories burned, time, and date. The code then checks the status codes of the API responses to ensure that the data was successfully sent to the spreadsheet.
# To complete the code, you need to replace the placeholders in the code with your actual API keys and endpoint URLs.

# Replace YOUR_API_KEY in nutritionix_api_key with your Nutritionix API key.
# Replace YOUR_APP_ID in the nutritionix_headers dictionary with your Nutritionix app ID.
# Replace YOUR_API_KEY in the sheety_endpoint URL with your Sheety API key.
# Replace exerciseData in the sheety_endpoint URL with the name of your Google Sheets spreadsheet.
# Once you have replaced these placeholders, you should be able to run the code and see the exercise information being sent to your Google Sheets spreadsheet.

# Note: You may also need to install the requests library if you don't already have it installed. You can do this by running pip install requests in your terminal or command prompt.


import requests
import datetime as dt

# Define the Nutritionix API endpoint and API key
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_api_key = "YOUR_API_KEY"

# Define the headers for the Nutritionix API request
nutritionix_headers = {
    "x-app-id": "YOUR_APP_ID",
    "x-app-key": nutritionix_api_key,
    "Content-Type": "application/json"
}

# Define the Sheety API endpoint
sheety_endpoint = "https://api.sheety.co/YOUR_API_KEY/exerciseData"

# Define the exercise description to query
exercise = "ran for 30 minutes"

# Define the payload for the Nutritionix API request
nutritionix_payload = {
    "query": exercise
}

# Make a request to the Nutritionix API
nutritionix_response = requests.post(nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_payload)

# Check if the request was successful
if nutritionix_response.status_code == 200:
    # Extract the exercise information from the response
    nutritionix_data = nutritionix_response.json()
    exercise = nutritionix_data['exercises'][0]['name']
    duration = nutritionix_data['exercises'][0]['duration_min']
    calories = nutritionix_data['exercises'][0]['nf_calories']
    time = dt.datetime.now().strftime("%H:%M:%S")
    date = dt.datetime.now().strftime("%d/%m/%Y")
    
    # Define the payload for the Sheety API request
    sheety_payload = {
        "exercise": exercise,
        "duration": duration,
        "calories": calories,
        "time": time,
        "date": date
    }
    
    # Make a request to the Sheety API
    sheety_response = requests.post(sheety_endpoint, json=sheety_payload)
    
    # Check if the request was successful
    if sheety_response.status_code == 200:
        print("Exercise information successfully sent to Google Sheets.")
    else:
        # Print the error message
        print("Error sending data to Google Sheets: {}".format(sheety_response.json()["error"]))
else:
    # Print the error message
    print("Error: {}".format(nutritionix_response.json()["message"]))
