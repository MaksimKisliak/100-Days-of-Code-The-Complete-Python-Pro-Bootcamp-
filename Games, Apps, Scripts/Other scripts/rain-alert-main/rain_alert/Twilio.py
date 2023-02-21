from twilio.rest import Client


class TwilioSMS:

    def __init__(self):
        self.forecast_period = None
        self.account_sid = "#"
        self.auth_token = "#"
        self.client = Client(self.account_sid, self.auth_token)  # if one of ids is less than 700, then message me

    def message_take_umbrella(self):
        message = self.client.messages.create(
            body=f"В течение следующих {self.forecast_period*3} часа/-ов пойдет дождь, поэтому не забудь взять с собой зонт ☔️",
            from_="+13854690615",
            to="+48881556487"
        )
        print(message.sid)

    def message_do_not_take_umbrella(self):
        message = self.client.messages.create(
            body=f"В течение следующих {self.forecast_period*3} часа/-ов не пойдет дождь, поэтому забудь о зонте ☔️",
            from_="+13854690615",
            to="+48881556487"
        )
        print(message.sid)
