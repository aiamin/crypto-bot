import pandas as pd
import pandas_ta as ta
import ccxt
import requests

exchange = ccxt.coinex()

discord_webhook_url = "https://discord.com/api/webhooks/962754927896195103/rC9nH7foyWOmQGpa9LRBOUF3s390UQe_1Lgs_S9I6FLmCVXvupY9_ZUXDHPuFvA5JxBI"


bars1 = exchange.fetch_ohlcv('BTC/USDT', timeframe='5m', limit=500)
df1 = pd.DataFrame(bars1, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

adx1 = df1.ta.adx()
macd1 = df1.ta.macd(fast=14, slow=28)
rsi1 = df1.ta.rsi()

df1 = pd.concat([df1, adx1, macd1, rsi1], axis=1)

last_row_1 = df1.iloc[-1]

if last_row_1['ADX_14'] >= 25:
    if last_row_1['DMP_14'] > last_row_1['DMN_14']:
        message1 = f"**BTC STRONG UPTREND**: The ADX is {last_row_1['ADX_14']:.2f}"
        print(message1)
    if last_row_1['DMN_14'] > last_row_1['DMP_14']:
        message1 = f"**BTC STRONG DOWNTREND**: The ADX is {last_row_1['ADX_14']:.2f}"
        print(message1)
    # payload = {
    #     "username": "BTCalertbot",
    #     "content": message1
    # }
    # requests.post(discord_webhook_url, json=payload)

if last_row_1['ADX_14'] < 25:
    message1 = f"**BTC NO TREND**: The ADX is {last_row_1['ADX_14']:.2f}"
    print(message1)
    # payload = {
    #     "username": "BTCalertbot",
    #     "content": message1
    # }
    # requests.post(discord_webhook_url, json=payload) 




bars2 = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
df2 = pd.DataFrame(bars2, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

adx2 = df2.ta.adx()
macd2 = df2.ta.macd(fast=14, slow=28)
rsi2 = df2.ta.rsi()

df2 = pd.concat([df2, adx2, macd2, rsi2], axis=1)

last_row_2 = df2.iloc[-1]

if last_row_2['ADX_14'] >= 25:
    if last_row_2['DMP_14'] > last_row_2['DMN_14']:
        message2 = f"**ETH STRONG UPTREND**: The ADX is {last_row_2['ADX_14']:.2f}"
        print(message2)
    if last_row_2['DMN_14'] > last_row_2['DMP_14']:
        message2 = f"**ETH STRONG DOWNTREND**: The ADX is {last_row_2['ADX_14']:.2f}"
        print(message2)
    # payload = {
    #     "username": "ETHalertbot",
    #     "content": message2
    # }
    # requests.post(discord_webhook_url, json=payload)

if last_row_2['ADX_14'] < 25:
    message2 = f"**ETH NO TREND**: The ADX is {last_row_2['ADX_14']:.2f}"
    print(message2)
    # payload = {
    #     "username": "ETHalertbot",
    #     "content": message2
    # }
    # requests.post(discord_webhook_url, json=payload) 

message_end = message1 + '\n' + message2

payload = {"username": "alertbot","content": message_end }

requests.post(discord_webhook_url, json=payload)