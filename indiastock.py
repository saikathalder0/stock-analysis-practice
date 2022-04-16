URL = "https://query1.finance.yahoo.com/v8/finance/chart/INFY.NS?region=IN&lang=en-IN&includePrePost=false&interval=1m&range=1d&corsDomain=in.finance.yahoo.com&.tsrc=finance"
import requests
resp = requests.get(URL)
print(resp.text)