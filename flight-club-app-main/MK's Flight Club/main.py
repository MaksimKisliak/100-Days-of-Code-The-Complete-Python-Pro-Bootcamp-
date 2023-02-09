from datetime import datetime, timedelta
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


class MainLogic:
    """
    Class to hold the main logic of the flight searching and email notification process.
    """

    def __init__(self):
        # self.sheety_destination_data = DataManager().sheety_destination_data['prices']  #live destinations data
        # Assign sample data to `sheety_destination_data` for testing purposes
        self.sheety_destination_data = [
            {"city": "Paris", "iataCode": "PAR", "lowestPrice": 54},
            {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42},
            {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485},
            {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551},
            {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95},
            {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414},
            {"city": "New York", "iataCode": "NYC", "lowestPrice": 240},
            {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260},
            {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378},
            {"city": "Bali", "iataCode": "DPS", "lowestPrice": 501}
        ]
        # self.sheety_customers_data = DataManager().sheety_customers_data['users']  #live users data
        # Assign sample data to `sheety_customers_data` for testing purposes
        self.sheety_customers_data = [{"First Name": "Maksim", "Last Name": "Kisliak", "Email": "makskislyak@gmail.com"},
                                      # {"First Name": "Marharyta", "Last Name": "Yudina", "Email": "ritayud@gmail.com"},
                                      # {"First Name": "Marharyta", "Last Name": "Yudina", "Email": "ritayud21@gmail.com"}
                                      ]
        self.now = datetime.now()
        self.tomorrow = self.now + timedelta(days=1)
        self.half_a_year = self.now + timedelta(days=6 * 30)

    def search_destination_code(self):
        """
        Fetch IATA codes for each city in `sheety_destination_data` via kiwi location API.
        """
        # Loop through each city in `sheety_destination_data`
        for each_city in self.sheety_destination_data:
            destination_city = each_city['city']
            row_id = each_city['id']
             # Fetch IATA code using `FlightSearch().search_destination_code()` method
            iata_code = FlightSearch().search_destination_code(city=destination_city)
            # Save IATA code using `DataManager().put_destination_code()` method
            iata_code_to_put = DataManager()
            print(iata_code_to_put.put_destination_code(iata_code, row_id))

    def check_flights(self):
        """
        This function iterates through the list of destination data and finds the cheapest flight for each destination.
        If a flight is found with a lower price, an alert email is sent to the customer with details of the flight.
        """
        # Loop through each city in `sheety_destination_data`
        for each_city in self.sheety_destination_data:
            # Get the IATA code of the destination city
            destination_city_code = each_city['iataCode']
            # Search for the cheapest flight using the FlightSearch class
            flight = FlightSearch().search_cheapest(origin_city_code='LON',
                                                    destination_city_code=destination_city_code,
                                                    from_time=self.tomorrow,
                                                    to_time=self.half_a_year)
            # If flight is not found, skip to next iteration
            if flight is None:
                continue
            # Check if the price of the flight is lower than the previous lowest price
            elif each_city['lowestPrice'] > flight.price:
                # Check for number of stopovers and connections
                # If stopovers=0 and connections=2
                if flight.stopovers == 0 and flight.connection_number == 2:
                    # Create the message text with flight details
                    text = f'Low price alert! Your lowest price from {flight.origin_city}-{flight.origin_airport} ' \
                           f'to {flight.destination_city}-{flight.destination_airport} is £{each_city["lowestPrice"]}. ' \
                           f'From {flight.out_date} to {flight.return_date}. ' \
                           f'Price of the ticket found is £{flight.price}. ' \
                           f'Stopovers number is {flight.stopovers}, connections number is {flight.connection_number}.\n' \
                           f'Here\'s a link to book your flight: {flight.google_link}.'
                    # notification = NotificationManager()
                    # notification.send_message(text)
                    # Loop through each customer in `sheety_customers_data`
                    # and send the email using NotificationManager class
                    for each_user in self.sheety_customers_data:
                        NotificationManager().send_email(text, each_user['Email'])
                  # Print the message text for testing purposes
                    print(text)
                 # If stopovers=1 and connections=3
                elif flight.stopovers == 1 and flight.connection_number == 3:
                   # Create the message text with flight details
                    text = f'Low price alert! Your lowest price from {flight.origin_city}-{flight.origin_airport}' \
                           f' to {flight.destination_city}-{flight.destination_airport} is £{each_city["lowestPrice"]}. ' \
                           f'From {flight.out_date} to {flight.return_date}. Price of the ticket found is £{flight.price}.' \
                           f' Stopovers number is {flight.stopovers}, connections number is {flight.connection_number} ' \
                           f'via {flight.via_city[0]}.\nHere\'s a link to book your flight: {flight.google_link}.'
                    # notification = NotificationManager()
                    # notification.send_message(text)
                  # Loop through each customer in `sheety_customers_data`
                    for each_user in self.sheety_customers_data:
                        # Send the email with the flight information
                        NotificationManager().send_email(text, each_user['Email'])
                    # Print the message text for testing purposes
                    print(text)
                
                elif flight.stopovers == 2 and flight.connection_number == 4:
                    text = f'Low price alert! Your lowest price from {flight.origin_city}-{flight.origin_airport}' \
                           f' to {flight.destination_city}-{flight.destination_airport} is £{each_city["lowestPrice"]}. ' \
                           f'From {flight.out_date} to {flight.return_date}. Price of the ticket found is £{flight.price}.' \
                           f' Stopovers number is {flight.stopovers}, connections number is {flight.connection_number} ' \
                           f'via {flight.via_city[0]}.\nHere\'s a link to book your flight: {flight.google_link}.'
                    # notification = NotificationManager()
                    # notification.send_message(text)
                    
                    for each_user in self.sheety_customers_data:
                        NotificationManager().send_email(text, each_user['Email'])
                    print(text)

    def add_user_to_google_sheet(self):  # adding new user into the club
        print('Welcome to MK\'s Flight Club.\nWe find the best flight deals and email you.')
        first_name = input('What is your first name?\n')
        last_name = input('What is your last name?\n')
        member_email = input('What is your email?\n')
        member_email_2_time = input('Type your email again.\n')
        member_email_check = member_email == member_email_2_time
        if member_email_check:
            DataManager().put_new_user(first_name, last_name, member_email)
            print('You\'re in the club!')


# MainLogic().add_user_to_google_sheet()
MainLogic().check_flights()
