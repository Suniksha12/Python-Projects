from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        

test = ["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
        "My name is Suniksha Patel","Welcome to Whoosh-tech You tube channel"]

test1 = r.choice(test)

print("***** tying speed *****")
print(test1)

#Now we will take the user input
#Now we will take 2 line breaks
print()
print()

testinput = input(" Enter : ")

"""Now we need Following Thing:
   1) Speed Calculation
   2) Error Checking
   3) Function Defining"""

