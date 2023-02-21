from twilio.rest import Client


class SMS:

    def __init__(self):
        self.account_sid = ""
        self.auth_token = ""
        self.client = Client(self.account_sid, self.auth_token)

    def message(self, content):
        message = self.client.messages.create(
            body=content,
            from_="+13854690615",
            to="+48..."
        )
        print(message.sid)

