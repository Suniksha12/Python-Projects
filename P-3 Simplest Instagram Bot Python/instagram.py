# from instabot import Bot 
# # with this we can upload photo , follow and unfollow any person if we want
# bot = Bot()
# #login into the system
# bot.login(username="nooob_businessman98",password="sahimkhan123")
# bot.follow("ishowspeed")

# #how to uplaod photo in insta for this put the image in the same directory
# """Also make sure you copy & paste the path and change the slash to /"""
# # bot.upload_photo("C:\Users\sunik\OneDrive\Desktop\Python Projects\P-3 Simplest Instagram Bot Python")


from instagrapi import Client

cl = Client()
cl.login("nooob_businessman98", "sahimkhan123")
# user_id = cl.user_id_from_username("ishowspeed")
# cl.user_follow(user_id)

#Now i need to upalod photo onto the id
"""Install the library pip install instagrapi"""
from instagrapi import Client

# Initialize the client
# cl = Client()

# # Login to Instagram
# username = "your_username"
# password = "your_password"
# cl.login(username, password)

# Path to the photo and caption
photo_path = "WHOOSH.png"  # Replace with the path to your photo
caption = "This is a test upload from a bot! 🚀 #PythonBot"

# Upload the photo
media = cl.photo_upload(photo_path, caption)
print(f"Photo uploaded successfully: {media.dict()}")
