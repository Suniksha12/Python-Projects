from skpy import Skype

slogin = Skype("sunikshabenpatel@gmail.com","sunikSha17@")

#you can also give messages using the [] after contacts and giving thier skype ids 
contact = slogin.contacts["live:.cid.2405d0ce58c715aa"]

contact.chat.sendMsg("Welcome to Whoosh-Tech")



# for i in contact:
#     print(i)