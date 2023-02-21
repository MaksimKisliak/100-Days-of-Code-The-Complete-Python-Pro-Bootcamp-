import os
import requests
from flight_data import FlightData


# FlightSearch class for searching for flights using Tequila/Kiwi API
class FlightSearch:
    """This class is responsible for talking to the Flight Search API"""
    def __init__(self):
        # Get the API key from environment variable 'TEQUILA_KIWI_API_KEY'
        self.api_key = os.environ.get('TEQUILA_KIWI_API_KEY')

        # Set the header for the API request with the API key
        self.headers = {'apikey': self.api_key}

        # Get the location endpoint from environment variable 'TEQUILA_KIWI_LOCATION_QUERY_ENDPOINT'
        self.location_endpoint = os.environ.get('TEQUILA_KIWI_LOCATION_QUERY_ENDPOINT')

        # Get the search endpoint from environment variable 'TEQUILA_KIWI_SEARCH_QUERY_ENDPOINT'
        self.search_endpoint = os.environ.get('TEQUILA_KIWI_SEARCH_QUERY_ENDPOINT')

    # Function to get destination code for the given city
    def search_destination_code(self, city):
        # Query parameter for location API request
        query = {'term': city,
                 'locale': 'en-US',
                 'location_types': 'city',
                 'limit': '1',
                 'active_only': 'true'
                 }

        # Make a GET request to the location endpoint with the query parameters and headers
        result = requests.get(url=self.location_endpoint,
                              headers=self.headers,
                              params=query).json()['locations'][0]['code']
        
        # Return the destination code
        return result

    # Function to search for the cheapest flight
    def search_cheapest(self, origin_city_code, destination_city_code, from_time, to_time):
    """Search for the cheapest flight between the origin and destination city codes 
    within the specified date range.
    
    :param origin_city_code: code of the city to fly from
    :param destination_city_code: code of the city to fly to
    :param from_time: start date of the search range
    :param to_time: end date of the search range
    :return: FlightData object containing the flight details"""
      # Define parameters for searching for flights with 0, 1, and 2 stopovers
        query_0_stopovers = {"fly_from": origin_city_code,
                             "fly_to": destination_city_code,
                             "date_from": from_time.strftime("%d/%m/%Y"),
                             "date_to": to_time.strftime("%d/%m/%Y"),
                             "nights_in_dst_from": 7,
                             "nights_in_dst_to": 28,
                             "flight_type": "round",
                             "one_for_city": 1,
                             "max_stopovers": 0,
                             "curr": "GBP"
                             }

        query_1_stopovers = {"fly_from": origin_city_code,
                             "fly_to": destination_city_code,
                             "date_from": from_time.strftime("%d/%m/%Y"),
                             "date_to": to_time.strftime("%d/%m/%Y"),
                             "nights_in_dst_from": 7,
                             "nights_in_dst_to": 28,
                             "flight_type": "round",
                             "one_for_city": 1,
                             "max_stopovers": 1,
                             "curr": "GBP"
                             }

        query_2_stopovers = {"fly_from": origin_city_code,
                             "fly_to": destination_city_code,
                             "date_from": from_time.strftime("%d/%m/%Y"),
                             "date_to": to_time.strftime("%d/%m/%Y"),
                             "nights_in_dst_from": 7,
                             "nights_in_dst_to": 28,
                             "flight_type": "round",
                             "one_for_city": 1,
                             "max_stopovers": 2,
                             "curr": "GBP"
                             }
        # First try to get the flight data for 0 stopovers
        try:
             # Send a GET request to the API with the query parameters
            result = requests.get(url=self.search_endpoint,
                                  headers=self.headers,
                                  params=query_0_stopovers).json()["data"][0]
            # Store the flight details in a FlightData object
            result = FlightData(
                price=result['price'],
                origin_city=result['cityFrom'],
                origin_airport=result['flyFrom'],
                destination_city=result['cityTo'],
                destination_airport=result['flyTo'],
                out_date=result['local_departure'].split('T')[0],
                return_date=result['route'][1]['local_arrival'].split('T')[0],
                link=result['deep_link'],
                google_link=f"https://www.google.co.uk/flights?hl=en#flt={result['flyFrom']}.{result['flyTo']}.{result['local_departure'].split('T')[0]}*{result['flyTo']}.{result['flyFrom']}.{result['route'][3]['local_arrival'].split('T')[0]}",
                stopovers=0,
                via_city=None,
                connection_number=len(result['route'])
            )
            print(f'{result.destination_city}: £{result.price}')
            return result

        except IndexError:
            try:
                result = requests.get(url=self.search_endpoint,
                                      headers=self.headers,
                                      params=query_1_stopovers).json()["data"][0]
                result = FlightData(
                    price=result['price'],
                    origin_city=result['cityFrom'],
                    origin_airport=result['flyFrom'],
                    destination_city=result['cityTo'],
                    destination_airport=result['flyTo'],
                    out_date=result['local_departure'].split('T')[0],
                    return_date=result['route'][2]['local_arrival'].split('T')[0],
                    link=result['deep_link'],
                    google_link=f"https://www.google.co.uk/flights?hl=en#flt={result['flyFrom']}.{result['flyTo']}.{result['local_departure'].split('T')[0]}*{result['flyTo']}.{result['flyFrom']}.{result['route'][3]['local_arrival'].split('T')[0]}",
                    stopovers=1,
                    via_city=result['route'][0]['cityTo'],
                    connection_number=len(result['route'])
                )
                print(f'{result.destination_city}: £{result.price}')
                return result

            except IndexError:
                try:
                    result = requests.get(url=self.search_endpoint,
                                          headers=self.headers,
                                          params=query_2_stopovers).json()["data"][0]
                    result = FlightData(
                        price=result['price'],
                        origin_city=result['cityFrom'],
                        origin_airport=result['flyFrom'],
                        destination_city=result['cityTo'],
                        destination_airport=result['flyTo'],
                        out_date=result['local_departure'].split('T')[0],
                        return_date=result['route'][3]['local_arrival'].split('T')[0],
                        link=result['deep_link'],
                        google_link=f"https://www.google.co.uk/flights?hl=en#flt={result['flyFrom']}.{result['flyTo']}.{result['local_departure'].split('T')[0]}*{result['flyTo']}.{result['flyFrom']}.{result['route'][3]['local_arrival'].split('T')[0]}",
                        stopovers=2,
                        via_city=result['route'][0]['cityTo'],
                        connection_number=len(result['route'])
                    )
                    print(f'{result.destination_city}: £{result.price}')
                    return result

                except IndexError:
                    print(f'No flights found for {destination_city_code}')
                    return None


