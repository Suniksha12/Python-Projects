# from instabot import Bot 
# # with this we can upload photo , follow and unfollow any person if we want
# bot = Bot()
# #login into the system
# bot.login(username="nooob_businessman98",password="sahimkhan123")
# bot.follow("ishowspeed")

# #how to uplaod photo in insta for this put the image in the same directory
# """Also make sure you copy & paste the path and change the slash to /"""

from instagrapi import Client

cl = Client()
cl.login("nooob_businessman98", "sahimkhan123")
# user_id = cl.user_id_from_username("ishowspeed")
# cl.user_follow(user_id)

#Now i need to upalod photo onto the id
# Path to the photo and caption
# photo_path = "WHOOSH.png"  # Replace with the path to your photo
# caption = "This is a test upload from a bot! 🚀 #PythonBot"

# # Upload the photo
# media = cl.photo_upload(photo_path, caption)
# print(f"Photo uploaded successfully: {media.dict()}")

# """How to Unfollow the person"""
# # Retrieve the user ID of the person you want to unfollow
# user_id = cl.user_id_from_username("ishowspeed")

# # Unfollow the user
# cl.user_unfollow(user_id)
# print(f"Successfully unfollowed the user with ID: {user_id}")

#how to send message to multiple person
# Send message to multiple users
# import time 
# import random

# cl.delay_range=[3,7]
# usernames = ["businessometrix", "ishowspeed"]  # Replace with actual usernames
# try:
#     # Get User IDs
#     user_ids = [cl.user_info_by_username(username).pk for username in usernames]

#     # Message to send
#     message = "Hello! How u doin??"

#     # Send messages
#     for user_id in user_ids:
#         cl.direct_send(text=message, user_ids=[user_id])
#         print(f"Message sent successfully to {user_id}")
#         time.sleep(random.randint(5, 10))  # Random delay to mimic human behavior

# except Exception as e:
#     print("Error:", e)

#followers information list
# Get user ID from username
user_id = cl.user_id_from_username("nooob_businessman98")

# Fetch followers (returns a dictionary {user_id: timestamp})
followers_dict = cl.user_followers(user_id)

# Extract user IDs from dictionary
followers_list = list(followers_dict.keys())

# Print follower details
for follower_id in followers_list:
    user_info = cl.user_info(follower_id)
    print(f"Username: {user_info.username}, Full Name: {user_info.full_name}")


