import pandas as pd
import pandas_ta as ta
import ccxt

exchange = ccxt.coinex()

bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='5m', limit=500)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'clode', 'volume'])

print(df)