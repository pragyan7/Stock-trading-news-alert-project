import requests
from twilio.rest import Client

STOCK_NAME = "your_stock_name"
COMPANY_NAME = "your_company_name"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "your_stock_api_key"
NEWS_API_KEY = "your_news_api_key"

TWILIO_SID = "your_twilio_account_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
    # When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

    #1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data['4. close']

    #2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

    #3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

    #4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((difference / float(yesterday_closing_price))*100)

    #5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 5:
    ## STEP 2: https://newsapi.org/ 
    # 6. - Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    #7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]

## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #8. - Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    #to send a separate message with each article's title and description to your phone number. 
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

#9. - Send each article as a separate message via Twilio. 
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_="your_twilio_phone_number",
            to="your_phone_number",
        )
