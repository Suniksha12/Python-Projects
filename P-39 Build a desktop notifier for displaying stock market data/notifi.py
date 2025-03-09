import datetime
import time
from plyer import notification

while True:
    notification.notify(
        title="To-Do List ({})".format(datetime.date.today()),  # Fixed title formatting
        message="1. Live classes \n2. Projects \n3. Presentation",
        app_icon=r"C:\Users\sunik\OneDrive\Desktop\Python Projects\P-39 Build a desktop notifier for displaying stock market data\Alecive-Flatwoken-Apps-Notifications.ico",  # Use .ico
        timeout=10
    )
    time.sleep(10)

#for the icons parts go to the link provided - https://www.iconarchive.com/search?q=application+.ico&page=7