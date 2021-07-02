import os
import alpaca_trade_api as alpaca
import requests
from config import *

ACCOUNT_URL = ("{}" + ACCOUNT_ENDPOINT).format(BASE_URL)
r = requests.get(ACCOUNT_URL, headers={'APCA-API-KEY-ID': API_KEY, 'APCA-API-SECRET-KEY': SECRET_KEY})

print(ACCOUNT_URL)
print(r.content)