#create a python file with extension .py

email = input("Enter your Email : ") #g@g.in i have used 6 characters in this gmail

#i got the string as an input 
#Conditions
k=0,j=0,d=0
if(len(email)>=6):
    #pass
    if(email[0].isalpha()):
        # pass
        #membership operator
        if("@" in email) and (email.count("@")==1):
            #pass
            if(email[-4]==".") ^ (email[-3]=="."):
                #pass
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper(): 
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("WRONG EMAIL 5");
            else:
                print("WRONG EMAIL 4");
        else:
            print("WRONG EMAIL 3")
    else:
        print("WRONG EMAIL 2")
else:
    print("WRONG EMAIL 1 ")