from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="*** Take Rest ***",
            message= "Rest is vital for better mental health, increased concentration and memory, a healthier immune system, reduced stress, improved mood and even a better metabolism",
            app_icon = r"C:/Users/sunik/OneDrive/Desktop/Python Projects/P-14 Desktop Notifier for Python/rest_icon.ico",
            timeout=5
        )
        time.sleep(60*60)

#for stopping the notification press Ctrl + c 
#also if you have your image in .png or .jpg or jpeg then try to convert it 
#using an online converter convert it into a .ico  i.e convert it into icon.