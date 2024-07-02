# Stock-trading-news-alert-project
This repository contains a project for a stock trading news alert system. It leverages the News API to gather the latest news related to stock trading and the Alpha Vantage API to monitor stock prices. The alerts are then sent directly to your phone using Twilio.

## Features
* News Monitoring: Fetches the latest stock trading news using the News API.
* Stock Price Monitoring: Retrieves real-time stock prices using the Alpha Vantage API.
* Alert System: Sends alerts to your phone via Twilio.
* Customizable Settings: Easily configure the stock symbols and news topics you want to track.

## Technologies Used
* Python: Core programming language for implementing the alert system.
* News API: Provides the latest news articles related to stock trading.
* Alpha Vantage API: Fetches real-time stock prices and updates.
* Twilio API: Sends SMS alerts to your phone.

## Configuration
* Obtain API keys from News API, Alpha Vantage, and Twilio.
* Create a .env file in the project directory and add your API keys and phone number:
```python
NEWS_API_KEY=your_news_api_key
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
YOUR_PHONE_NUMBER=your_phone_number
```
* Customize the config.json file to specify the stock symbols and news topics you want to monitor.

## Usage
* Run the main script to start monitoring news and stock prices:
```
python main.py
```
