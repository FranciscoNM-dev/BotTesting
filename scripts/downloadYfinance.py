import yfinance as yf
import pandas as pd
import os

df = yf.download('MSFT', period="1y", interval="1d", auto_adjust=True, group_by='ticker')
repoRoute = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dataRoute = os.path.join(repoRoute, 'data')


df.to_csv(path_or_buf = os.path.join(dataRoute, 'ejemploMSFT.csv'))
