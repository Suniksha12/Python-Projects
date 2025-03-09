import datetime
import time
from plyer import notification

notification.notify(
    title = "To-Do List".format(datetime.date.today()),
    message = "1. live classes \n2. projects \n3. presentation"
)

#for the icons parts go to the link provided - https://www.iconarchive.com/search?q=application+.ico&page=7