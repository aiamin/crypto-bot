import pandas as pd
import pandas_ta as ta
import ccxt
import requests

exchange = ccxt.coinex()

discord_webhook_url = "https://discord.com/api/webhooks/962754927896195103/rC9nH7foyWOmQGpa9LRBOUF3s390UQe_1Lgs_S9I6FLmCVXvupY9_ZUXDHPuFvA5JxBI"

bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])

adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)
rsi = df.ta.rsi()

df = pd.concat([df, adx, macd, rsi], axis=1)

last_row = df.iloc[-1]




if last_row['ADX_14'] >= 25:
    if last_row['DMP_14'] > last_row['DMN_14']:
        message = f"STRONG UPTREND: The ADX is {last_row['ADX_14']:.2f}"
        print(message)
    if last_row['DMN_14'] > last_row['DMP_14']:
        message = f"STRONG DOWNTREND: The ADX is {last_row['ADX_14']:.2f}"
        print(message) 
    payload = {
        "username": "alertbot",
        "content": message
    }
    requests.post(discord_webhook_url, json=payload)


if last_row['ADX_14'] < 25:
    message = f"NO TREND: The ADX is {last_row['ADX_14']:.2f}"
    print(message)
    payload = {
        "username": "alertbot",
        "content": message
    }
    requests.post(discord_webhook_url, json=payload)