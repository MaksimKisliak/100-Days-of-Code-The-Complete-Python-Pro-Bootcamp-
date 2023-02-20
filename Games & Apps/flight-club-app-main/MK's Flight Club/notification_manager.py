from twilio.rest import Client
import smtplib
import os


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details"""

    def __init__(self):
        self.account_sid = os.environ.get('TWILIO_SID')
        self.auth_token = os.environ.get('TWILIO_TOKEN')
        self.email = os.environ.get('EMAIL')
        self.email_password = os.environ.get('EMAIL_PASSWORD')
        self.client = Client(self.account_sid, self.auth_token)  # if one of ids is less than 700, then message me

    def send_message(self, text):
        message = self.client.messages.create(
            body=text,
            from_="+13854690615",
            to="+48881556487"
        )
        print(message.sid)

    def send_email(self, text, to_addrs):
        with smtplib.SMTP('smtp.mail.ru') as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.email_password)
            connection.sendmail(from_addr=self.email,
                                to_addrs=to_addrs,
                                msg=f'Subject: New Low Price Flight!\n\n{text}'.encode('utf-8'))
