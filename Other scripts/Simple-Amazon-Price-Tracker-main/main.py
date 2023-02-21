import smtplib
import requests
import lxml
from bs4 import BeautifulSoup

# Scrapes product information and price from an Amazon URL and sends a price alert email if the price is below a set threshold.

my_email = ''
password = ''


url = "https://www.amazon.com/Apple-MacBook-16-inch-10%E2%80%91core-16%E2%80%91core/dp/B09JQKBQSB"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
    "Accept-Language": "en-GB,en;q=0.9"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())


price = soup.find(name="span", class_="a-offscreen").getText()
price_without_currency = price.split("$")[1].replace(",", "")
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 2000  # Threshold price for the price alert email

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP('smtp.mail.ru', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f'Subject: Amazon Price Alert!\n\n{message}\n{url}'.encode('utf-8'))
