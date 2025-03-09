import datetime
import time
from plyer import notification

while True :
    notification.notify(
        title = "To-Do List".format(datetime.date.today()),
        message = "1. live classes \n2. projects \n3. presentation",
        app_icon = (r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-39 Build a desktop notifier for displaying stock market data\notifi.png"),
        timeout = 10
    )
    time.sleep(10)

#for the icons parts go to the link provided - https://www.iconarchive.com/search?q=application+.ico&page=7