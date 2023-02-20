import pandas
from random import choice, choices, randint
import smtplib
import datetime as dt

# Define email and password for authentication
my_email = 'makskislyak1@mail.ru'
password = 'APP_PASSWORD'
# List of letter templates for birthday greetings
letter_list = ['letter_templates/letter_1.txt', 'letter_templates/letter_2.txt', 'letter_templates/letter_3.txt']

# Data of people's birthdays to be appended to a CSV file
data_to_append = pandas.DataFrame([['Rita', 'ritayud@gmail.com', 2022, 12, 21],
                                   ['Maks', 'makskislyak@gmail.com', 2022, 12, 22]],
                                  columns='name email year month day'.split(" "))

# Append data to the CSV file
data_to_append.to_csv('birthdays.csv', index=False)
# Read the birthdays data from the CSV file
birthdays_file = pandas.read_csv('birthdays.csv', )

# Get current date and time
now = dt.datetime.now()
# Iterate over the rows in the birthdays data
for index, row in birthdays_file.iterrows():
  # Check if the current day and month match a birthday in the data
    if birthdays_file.iloc[index, 3] == now.month and birthdays_file.iloc[index, 4] == now.day:
      # Choose a random letter template from the list
        random_letter = choice(letter_list)
        # Open the chosen letter template
        with open(file=random_letter) as file:
          # Read the text of the letter and replace [NAME] with the name of the person
            e_mail_text = file.read().replace('[NAME]', birthdays_file.iloc[index, 0])
            # Connect to the email server
            with smtplib.SMTP('smtp.mail.ru') as connection:
              # Start a secure connection
                connection.starttls()
                 # Login with the provided email and password
                connection.login(user=my_email, password=password)
                # Send the birthday greeting email to the email address in the data
                connection.sendmail(from_addr=my_email,
                                    to_addrs=birthdays_file.iloc[index, 1],
                                    msg=f'Subject: Happy Birthday\n\n{e_mail_text}')




