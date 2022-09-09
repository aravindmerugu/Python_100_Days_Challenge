import requests
from twilio.rest import Client
import html

TWILLIO_ACCOUNT_SID = "YOUR_TWILLIO_SID"
TWILLIO_AUTH_TOKEN = "YOUR_TWILLIO_AUTH_ID"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR_STOCK_API"
NEWS_API_KEY = "YOUR_NEWS_API_KEY"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for key, value in data.items()]

yesterday = data_list[0]
yesterday_close_price = yesterday["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_close_price = day_before_yesterday["4. close"]
difference = (float(yesterday_close_price) - float(day_before_yesterday_close_price))
diff_percent = round((difference/float(yesterday_close_price))*100)
up_down = None
if diff_percent > 0:
    up_down="⬆"
else:
    up_down="⬇"

print(yesterday_close_price)
print(day_before_yesterday_close_price)
print(difference)
print(diff_percent)

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(diff_percent) > 4:
    news_parameters ={
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    news_data=news_response.json()["articles"]
    top_three_articles = news_data[:3]
    formatted_articles = [f"{STOCK}: {up_down} {diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in top_three_articles]
    print(formatted_articles)

    client = Client(TWILLIO_ACCOUNT_SID, TWILLIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+12185177821',
            to='+919182669603'
        )


