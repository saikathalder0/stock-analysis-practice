import requests 
import json
import matplotlib.pyplot as plt

SYMBOL = "KEYS"
API_KEY = "QK4GRY63EQBGCLFS"
URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + SYMBOL + '&apikey=' + API_KEY
x = requests.get(URL)
data = x.text
dictx = json.loads(data)
meta_data = dictx["Meta Data"]

var = dictx["Time Series (Daily)"]
alldays = var.keys()

days = []

closing_prices = []



for day in alldays:

    days.append(day)
    closing_prices.append(float(var[day]['4. close']))
# print(days)
# print(closing_prices)
plt.plot( days, closing_prices)
plt.show()

    # print(day)

    # print(var[day]['4. close'])
