#create a python file with extension .py

email = input("Enter your Email : ") #g@g.in i have used 6 characters in this gmail

#i got the string as an input 
#Conditions

if(len(email)>=6):
    #pass
    if(email[0].isalpha()):
        # pass
        #membership operator
        if("@" in email) and (email.count("@")==1):
            #pass
            if(email[-4]==".") ^ (email[-3]=="."):
                #pass
                for()
            else:
                print("WRONG EMAIL 4");
        else:
            print("WRONG EMAIL 3")
    else:
        print("WRONG EMAIL 2")
else:
    print("WRONG EMAIL 1 ")