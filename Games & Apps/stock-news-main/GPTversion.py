# Note: You'll need to replace YOUR_ALPHAVANTAGE_API_KEY, YOUR_NEWSAPI_KEY, YOUR_TWILIO_PHONE_NUMBER, and YOUR_PHONE_NUMBER with your own API keys and phone numbers.
# To run this script daily, you can set up a cron job or use a task scheduler. Here's an example of how to set up a cron job on a Unix-based system:

# Open a terminal window.
# Type crontab -e and press enter.
# Add the following line at the end of the file:

0 9 * * * /usr/bin/python3 /path/to/script.py SYMBOL COMPANY_NAME

# This line will run the script every day at 9:00 AM using the Python 3 executable located at /usr/bin/python3. Replace /path/to/script.py with the path to your script file, and replace SYMBOL and COMPANY_NAME with the desired values.

# Note: The format of a cron job is minute hour day month day-of-week command. In this example, the script will run every day (day month day-of-week) at 9:00 AM (hour minute).

# Finally, you'll need to sign up for Twilio and NewsAPI to get the necessary API keys. Here's how:

# Go to https://twilio.com/ and sign up for a Twilio account. Once you're logged in, go to the Console and obtain your TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN. You'll also need to purchase a Twilio phone number, which you can do from the Console.
# Go to https://newsapi.org/ and sign up for a NewsAPI account. Once you're logged in, go to the API Key section to obtain your NEWSAPI_KEY.
# With these API keys, you'll be able to run the script and receive daily stock alerts based on the criteria you specified.

# It's worth mentioning some best practices to ensure the reliability and security of your code:

# Store the API keys securely and avoid hardcoding them in the script. You can store them as environment variables and access them in the script using the os module.
# Handle exceptions properly in the code to avoid unexpected behavior when an API request fails or the file I/O operation raises an error.
# Consider using a database instead of a file to store the previous price. This can be useful if you want to keep track of the price history for multiple stocks.
# Add logging to your code to keep track of when the script is run, what actions are performed, and what the results are.
# Test your code thoroughly before deploying it to production to make sure it works as expected and all errors are handled properly.
# By following these best practices, you can ensure that your script runs smoothly and provides reliable and secure stock alerts.

import requests
import json
from twilio.rest import Client

def get_price(symbol):
    # Use AlphaVantage API to get the latest stock price for the given symbol
    response = requests.get(f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={YOUR_ALPHAVANTAGE_API_KEY}')
    data = json.loads(response.text)
    return float(data['Global Quote']['05. price'])

def get_news(company_name):
    # Use NewsAPI to get the first 3 news pieces for the given company name
    response = requests.get(f'https://newsapi.org/v2/everything?q={company_name}&apiKey={YOUR_NEWSAPI_KEY}')
    data = json.loads(response.text)
    return [article['title'] for article in data['articles'][:3]]

def send_alert(message):
    # Use Twilio to send the message
    client = Client()
    message = client.messages \
                    .create(
                        body=message,
                        from_='YOUR_TWILIO_PHONE_NUMBER',
                        to='YOUR_PHONE_NUMBER'
                    )

def main(symbol, company_name):
    # Get the latest price
    current_price = get_price(symbol)
    # Get the previous price from a file or database
    try:
        with open('previous_price.txt', 'r') as f:
            previous_price = float(f.read())
    except FileNotFoundError:
        previous_price = current_price

    # Calculate the price change
    price_change = (current_price - previous_price) / previous_price * 100
    if abs(price_change) >= 5:
        message = f'The price of {symbol} has changed by {price_change:.2f}%.\n\n'
        news = get_news(company_name)
        message += '\n'.join(news)
        send_alert(message)

    # Update the previous price
    with open('previous_price.txt', 'w') as f:
        f.write(str(current_price))
