import ccxt
import pandas as pd

exchange = ccxt.kraken() # Kraken es muy bueno para pares en EUR
ohlcv = exchange.fetch_ohlcv('BTC/EUR', timeframe='1h', limit=1000)
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])