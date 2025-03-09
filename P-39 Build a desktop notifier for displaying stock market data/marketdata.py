# for this file open your command prompt in the same directory where you have saved your .py file
# and write the following command : pip install yfinance

import yfinance as yf

msft = yf.Ticker("MSFT")

print(msft.info)