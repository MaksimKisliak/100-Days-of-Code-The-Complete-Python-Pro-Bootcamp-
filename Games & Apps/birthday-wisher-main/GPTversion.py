import smtplib
import datetime
import json
from email.mime.text import MIMEText

# Define the SMTP server and port to use for sending email
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Define the sender and recipient email addresses
sender_email = "sender_email@gmail.com"

# Define the subject and body of the email
subject = "Happy Birthday!"
body = "Wishing you a very happy birthday filled with love, joy, and all your favorite things. May your day be as special as you are! Best wishes on your special day."

# Create a MIME text object for the email message
message = MIMEText(body)
message['subject'] = subject
message['From'] = sender_email

# Load the JSON file with birthdays
with open("birthdays.json") as f:
    birthdays = json.load(f)

# Check if today is anyone's birthday every day
while True:
    now = datetime.datetime.now()
    today = now.strftime("%m-%d")

    for person in birthdays:
        if today == person['birthday']:
            # Connect to the SMTP server and send the email
            message['To'] = person['email']
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.ehlo()
            server.starttls()
            server.login(sender_email, "sender_email_password")
            server.send_message(message)
            server.quit()

# The code loads a JSON file birthdays.json which contains information about people and their birthdays, using the json.load() function. 
# The JSON file should have the following format:

[
  {
    "name": "Person 1",
    "email": "person1@email.com",
    "birthday": "06-15"
  },
  {
    "name": "Person 2",
    "email": "person2@email.com",
    "birthday": "07-25"
  },
  ...
]

# The code then uses a for loop to check if today's date, obtained using datetime.datetime.now(), matches any of the birthdays in the JSON file. 
#  If it does, the code sends the birthday greeting email as before, then moves on to the next person.
# Make sure to replace sender_email@gmail.com with the actual email address, and replace sender_email_password with the password for 
# the sender email account. Also, make sure to update the birthdays.json file with the correct information.
# This code will run continuously, checking for birthdays every day. To make it run in the background, you can add a time.sleep() 
# function to pause the program for a specified amount of time, such as 24 hours, between each iteration of the while loop.
# Note that this code will run indefinitely until stopped manually, so it may be a good idea to add some error handling or 
# other checks to ensure that the program continues to run smoothly.

import smtplib
import datetime
import json
import time
from email.mime.text import MIMEText

# Define the SMTP server and port to use for sending email
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Define the sender and recipient email addresses
sender_email = "sender_email@gmail.com"

# Define the subject and body of the email
subject = "Happy Birthday!"
body = "Wishing you a very happy birthday filled with love, joy, and all your favorite things. May your day be as special as you are! Best wishes on your special day."

# Create a MIME text object for the email message
message = MIMEText(body)
message['subject'] = subject
message['From'] = sender_email

# Load the JSON file with birthdays
with open("birthdays.json") as f:
    birthdays = json.load(f)

# Check if today is anyone's birthday every day
while True:
    now = datetime.datetime.now()
    today = now.strftime("%m-%d")

    for person in birthdays:
        if today == person['birthday']:
            # Connect to the SMTP server and send the email
            message['To'] = person['email']
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.ehlo()
            server.starttls()
            server.login(sender_email, "sender_email_password")
            server.send_message(message)
            server.quit()

    # Pause for 24 hours before checking again
    time.sleep(24 * 60 * 60)

# Here is a sample birthdays.json file that you can use for testing the birthday wisher program:
# ou can add as many people to this file as you like, and their birthdays will be checked daily by the program. 
# If a person's birthday is today, an email will be sent to the address specified in the email field.
[
    {
        "name": "Person 1",
        "email": "person1@email.com",
        "birthday": "01-01"
    },
    {
        "name": "Person 2",
        "email": "person2@email.com",
        "birthday": "02-02"
    },
    {
        "name": "Person 3",
        "email": "person3@email.com",
        "birthday": "03-03"
    },
    {
        "name": "Person 4",
        "email": "person4@email.com",
        "birthday": "04-04"
    },
    {
        "name": "Person 5",
        "email": "person5@email.com",
        "birthday": "05-05"
    }
]

