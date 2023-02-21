import requests
import datetime as dt
from newsapi import NewsApiClient
from stocks_data import SMS

STOCK = "TSLA" # setting the stock symbol as TSLA
COMPANY_NAME = "Tesla Inc" # setting the company name as Tesla Inc
alpha_vantage_api_key = "#" # setting the alpha vantage API key

def get_change(current, previous): # defining a function to calculate the percentage change
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0 # return the absolute change in percentage
    except ZeroDivisionError:
        return 0



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

url = \
    f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={alpha_vantage_api_key}'
r = requests.get(url) # sending a GET request to the API
data = r.json() # parsing the response to a JSON objec

today = dt.datetime.today().strftime('%Y-%m-%d') # getting today's date in YYYY-MM-DD format
yesterday = (dt.datetime.today()-dt.timedelta(1)).strftime('%Y-%m-%d') # getting yesterday's date
dby = (dt.datetime.today()-dt.timedelta(2)).strftime('%Y-%m-%d') # getting the day before yesterday's date

yesterdays_close_value = float(data['Time Series (Daily)'][str(yesterday)]['4. close']) # getting yesterday's closing value
dby_close_value = float(data['Time Series (Daily)'][str(dby)]['4. close']) # getting the day before yesterday's closing value

diff_abs = get_change(yesterdays_close_value, dby_close_value) # getting the absolute change in percentage
diff = yesterdays_close_value - dby_close_value # getting the change in value

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

newsapi = NewsApiClient(api_key='#') # creating an instance of NewsApiClient

all_articles = newsapi.get_everything(q=COMPANY_NAME, # sending a GET request to the API
                                      from_param=str(dby), # setting the start date as the day before yesterday
                                      to=str(yesterday), # setting the end date as yesterday
                                      language='en', 
                                      sort_by='popularity') # relevancy = articles more closely related to q come first.
                                                            # popularity = articles from popular sources and publishers come first.
                                                            # publishedAt = newest articles come first.




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

if diff >= 5:
    top_3_articles = all_articles['articles'][:3]
    headlines = [each_artcile['title'] for each_artcile in top_3_articles]
    briefs = [each_artcile['description'] for each_artcile in top_3_articles]
    for each_items in range(0, 3):
        body = f"TSLA:{'🔺'if diff > 0 else '🔻'}{int(diff)}%\nHeadline: {headlines[each_items]}\nBrief: {briefs[each_items]}"
        twilio_object = SMS()
        twilio_object.message(body)

print(f"yesterdays_close_value: {yesterdays_close_value}, dby_close_value: {dby_close_value}")
