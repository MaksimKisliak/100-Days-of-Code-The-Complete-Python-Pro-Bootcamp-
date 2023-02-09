from OWA import OWAForecast
from Twilio import TwilioSMS
import time
import schedule


def just_do_it(forecast_period):
    # open weather api set_up
    forecast = OWAForecast()
    list_id = forecast.fetch_id(forecast_period)
    # Twilio set_up
    twilio_message = TwilioSMS()
    twilio_message.forecast_period = forecast_period
    if forecast.check_for_precipitations(list_id):
        twilio_message.message_take_umbrella()
    else:
        twilio_message.message_do_not_take_umbrella()


schedule.every().day.at("21:39").do(just_do_it, forecast_period=5)  # update time and forecast period argument (e.g. 1 stands for the first upcoming 3 hours daily forecast)

while True:
    schedule.run_pending()
    time.sleep(60)



