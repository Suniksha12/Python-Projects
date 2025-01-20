#create a python file with extension .py

email = input("Enter your Email : ") #g@g.in i have used 6 characters in this gmail

#i got the string as an input 
#Conditions

if(len(email)>=6):
    #pass
    if(email[0].isalpha()):
        pass
    else:
        print("WRONG EMAIL 2")
else:
    print("WRONG EMAIL 1 ")