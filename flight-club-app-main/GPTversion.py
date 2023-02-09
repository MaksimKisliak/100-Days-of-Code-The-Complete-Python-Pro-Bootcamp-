import requests
import json
import smtplib
import schedule
import time
import datetime

class FlightSearch:
    def __init__(self, budget, origin, destination, start_date, end_date, stay_duration):
        self.budget = budget
        self.origin = origin
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.stay_duration = stay_duration

    def search_flights(self):
        url = "https://api.tequilakiwi.com/flights"
        querystring = {"budget": self.budget, "origin": self.origin, "destination": self.destination, "start_date": self.start_date, "end_date": self.end_date, "stay_duration": self.stay_duration}
        response = requests.request("GET", url, params=querystring)
        flight_data = json.loads(response.text)
        return flight_data

class DataManager:
    def __init__(self):
        self.flight_data = []

    def add_flight_data(self, flight_data):
        self.flight_data.append(flight_data)

    def get_cheapest_flight(self):
        cheapest_flight = min(self.flight_data, key=lambda x: x['price'])
        return cheapest_flight

class EmailNotification:
    def __init__(self, recipient, flight_data):
        self.recipient = recipient
        self.flight_data = flight_data

    def send_email(self):
        subject = "Cheapest Flight Alert"
        body = f"The cheapest round flight from {self.flight_data['origin']} to {self.flight_data['destination']} is {self.flight_data['price']} from {self.flight_data['start_date']} to {self.flight_data['end_date']} with a stay duration of {self.flight_data['stay_duration']} days."
        message = f"Subject: {subject}\n\n{body}"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('your_email_address@gmail.com', 'your_email_password')
        server.sendmail('your_email_address@gmail.com', self.recipient, message)
        server.quit()

def flight_search_task():
    budget = 1000
    origin = "NYC"
    destination = "LON"
    start_date = datetime.datetime.now().strftime("%Y-%m-%d")
    end_date = (datetime.datetime.now() + datetime.timedelta(days=180)).strftime("%Y-%m-%d")
    stay_duration = "3-28"

    flight_search = FlightSearch(budget, origin, destination, start_date, end_date, stay_duration)
    flight_data = flight_search.search_flights()
    data_manager = DataManager()
    
data_manager.add_flight_data(flight_data)
cheapest_flight = data_manager.get_cheapest_flight()

email_notification = EmailNotification("recipient_email@example.com", cheapest_flight)
email_notification.send_email()

schedule.every(30).minutes.do(flight_search_task)

while True:
  schedule.run_pending()
  time.sleep(1)


# Note that the code has been modified to include the stay duration in the API call and search for round flights in the next 6 months. The email notification has also been updated to include the relevant flight information, such as start and end dates and stay duration.
# Additionally, the flight_search_task function runs every 30 minutes using the schedule library. The while loop at the end of the code ensures that the task is run continuously.

# Please make sure to replace 'your_email_address@gmail.com' and 'your_email_password' with your actual email address and password in the EmailNotification class, and also replace "recipient_email@example.com" with the email address of the recipient.

# # It's important to note that Tequila Kiwi API is not a real API, it's just an example API used in this code, so you need to replace it with a real API or another API that suits your needs.
# It's also important to consider the rate limiting and usage restrictions of the API you choose to use, as making too many requests too quickly can lead to your IP being blocked or rate limited by the API provider. You should check the API documentation for more information on rate limiting and usage restrictions.

# In conclusion, this code provides a basic framework for building a flight search app that uses a class-based structure and the Tequila Kiwi API to search for the cheapest flights to specific cities, within a specified budget and stay duration. The code runs continuously, checking for updates every 30 minutes, and sends an email notification with the relevant flight information to a specified recipient.
