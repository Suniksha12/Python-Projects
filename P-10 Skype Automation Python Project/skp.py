from skpy import Skype
import os.path

slogin = Skype("sunikshabenpatel@gmail.com","sunikSha17@")

#we will use file for the system and try to send it
contact = slogin.contacts["live:.cid.9bb5de17a53fab21"]
# we access the file and copy paste the file path also we will read it as binary
with open("C:/Users/sunik/OneDrive/Desktop/Python Projects/P-10 Skype Automation Python Project/download.png","rb") as f:
    contact.chat.sendFile(f,"download.png",image=True)

# Replace these with valid contact IDs
# contact_ids = ["live:.cid.9bb5de17a53fab21", "live:.cid.2405d0ce58c715aa"]

# try:
#     group = slogin.chats.create(contact_ids)
#     group.sendMsg("Welcome to the group from Whoosh-Tech!")
#     print("Group created and message sent successfully.")
# except Exception as e:
#     print(f"Error: {e}")

#you can also give messages using the [] after contacts and giving thier skype ids 
# contact = slogin.contacts
# contact.chat.sendMsg("Welcome to Whoosh-Tech")

# try:
#     contact = slogin.contacts["live:.cid.9bb5de17a53fab21"]
#     contact.chat.sendMsg("Welcome to Whoosh-Tech!")
#     print("Message sent successfully.")
# except Exception as e:
#     print(f"Error: {e}")


# for i in contact:
#     print(i)

# try:
#     for contact in slogin.contacts:
#         print(f"Contact ID: {contact.id}")
#         print(f"Name: {contact.name}")
#         print(f"Authorized: {contact.authorised}")
#         print(f"Blocked: {contact.blocked}")
#         print("-" * 30)
# except Exception as e:
#     print(f"Error: {e}")
