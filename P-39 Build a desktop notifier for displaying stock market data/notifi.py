import datetime
import time
from plyer import notification

import yfinance as yf
msft = yf.Ticker("MSFT")

data = msft.info

while True:
    notification.notify(
        title="MSFT data ({})".format(datetime.date.today()),  # Fixed title formatting
        message="Current Price = {cp} \nDayLow = {dl} \nDayHigh = {dh}".format(
            cp = data["currentPrice"],
            dl = data["regularMarketDayLow"],
            dh = data["regularMarketDayHigh"]
        ),
        app_icon=r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-39 Build a desktop notifier for displaying stock market data\Alecive-Flatwoken-Apps-Notifications.ico",  # Use .ico
        timeout=5
    )
    time.sleep(60 * 60 * 2)

#for the icons parts go to the link provided - https://www.iconarchive.com/search?q=application+.ico&page=7