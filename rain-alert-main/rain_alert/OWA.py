import requests


class OWAForecast:

    def __init__(self):
        """
        Initialize the required instance variables and make an API request to fetch the weather forecast
        """
        self.three_hours_forecast_list = None
        self.id_list_within_next_3_hour = None
        self.forecast_period = None
        self.params = {  # alternative way of fetching weather forecast by coordinates
            'lat': 52.229675,
            'lon': 21.012230
        }
        self.OWA_endpoint = 'api.openweathermap.org/data/2.5/forecast'
        self.api_key = '#'
        self.result = requests.get('http://api.openweathermap.org/data/2.5/forecast?'
                                   'lat=52.229675&'
                                   'lon=21.012230&'
                                   f'appid={self.api_key}')
        self.result.raise_for_status()

    def fetch_id(self, forecast_period):
        """
        Fetch weather ids for the provided forecast period

        :param forecast_period: Number of 3 hours forecast to retrieve
        :return: List of weather ids
        """
#         in order to change the amount of 3 hours forecast just simply modify forecast argument (e.g "1" means the first
#         upcoming 3 hours forecast, whereas "2" is fetching first two 3 hours forecasts)
        three_hours_forecast_argument = slice(forecast_period)  # argument for slicing method for the forecast list below
        self.three_hours_forecast_list = self.result.json()['list'][three_hours_forecast_argument]
        self.id_list_within_next_3_hour = [every_3_hour['weather'][0]['id'] for every_3_hour in self.three_hours_forecast_list]  # fetching all the ids from the forecast list
        print(self.id_list_within_next_3_hour)
        return self.id_list_within_next_3_hour

    def check_for_precipitations(self, list_id) -> bool:
        """
        Checks if all the ids in the provided list are less than 700. 
        Ids under 700 stand for Precipitations.

        :param list_id: list of weather ids
        :return: bool indicating whether all ids are less than 700
        """
        return all(int(i) < 700 for i in list_id)  # check each id in the new id list if it is less than 700 (all id less than 700 stands for "Precipitation")
