"""Email Validation in Python Using Regex Function
    a-Z
    0-9
    . _ time 1
    @ time 1
    . 2,3 index
 """

import re # regular expression 

email_condition = r"^[a-z]+[._]?[a-z0-9]+@[\w]+.[a-z]{2,3}$" #.com or .in

user_email = input(' Enter your Email : ')

if re.search(email_condition,user_email):
    print(" Right Email ")
else:
    print(" Wrong Email ")


