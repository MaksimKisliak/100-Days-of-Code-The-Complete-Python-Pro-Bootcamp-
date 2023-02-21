import os
import requests


class DataManager:
    """This class is responsible for talking to the Google Sheet"""
    def __init__(self):
        self.sheety_endpoint_prices = os.environ.get("SHEET_ENDPOINT_PRICES")
        self.sheety_endpoint_users = os.environ.get("SHEET_ENDPOINT_USERS")
        self.sheety_token = os.environ.get("TOKEN")
        self.sheety_headers = {'Authorization': self.sheety_token,
                               'Content-Type': 'application/json'}
        self.sheety_destination_data = {}
        self.sheety_customers_data = {}

    def get_destination_data(self):
#         This method retrieves the data for destinations from the endpoint using a GET request and the requests library. 
#         The result of the GET request is stored in the self.sheety_destination_data dictionary and returned.
        self.sheety_destination_data = requests.get(self.sheety_endpoint_prices, headers=self.sheety_headers).json()
        return self.sheety_destination_data

    def get_customers_data(self):
#         This method retrieves the data for customers from the endpoint using a GET request and the requests library. 
#         The result of the GET request is stored in the self.sheety_customers_data dictionary and returned.
        self.sheety_customers_data = requests.get(self.sheety_endpoint_users, headers=self.sheety_headers).json()
        return self.sheety_customers_data

    def put_destination_code(self, value, id):
#         This method updates the data for a destination by sending a PUT request to the endpoint. 
#         The value argument is the new value to be set for the price.iataCode field, 
#         and the id argument is the identifier for the destination being updated. 
#         The requests library is used to send the PUT request, which includes a JSON payload containing the updated data. 
#         The result of the PUT request is returned.
        query = {'price':
                     {'iataCode': value}
                 }
        result = requests.put(f'{self.sheety_endpoint_prices}/{id}', headers=self.sheety_headers, json=query).json()
        return result

    def put_new_user(self, firstName, lastName, email):
#         This method adds a new user by sending a POST request to the endpoint. 
#         The firstName, lastName, and email arguments are used to construct the JSON payload for the POST request. 
#         The requests library is used to send the POST request, and the result of the request is stored
        query = {'user':
                     {'firstName': firstName,
                      'lastName': lastName,
                      'email': email
                      }
                 }
        result = requests.post(f'{self.sheety_endpoint_users}', headers=self.sheety_headers, json=query).json()
        print('New user has been added', result)
