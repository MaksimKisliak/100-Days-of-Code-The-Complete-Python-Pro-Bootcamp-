import requests


# This code makes an API GET request to the "https://opentdb.com/api.php" URL with query parameters amount=10 and type=boolean. 
# The requests.get method returns a requests.Response object that represents the HTTP response. 
# The raise_for_status method raises an exception if the HTTP response indicates an error (status code >= 400).
# The response body is in JSON format, which is converted to a Python dictionary using the json() method. 
# The data variable now holds the response data, and question_data is assigned to the value of the "results" key in data, 
# which should contain an array of questions.

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
