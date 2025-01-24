"""Email Validation in Python Using Regex Function
    a-Z
    0-9
    . _ time 1
    @ time 1
    . 2,3 index
 """

import re

email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input(' Enter your Email : ')

if re.search(email_condition,user_email):
    print(" Right Email ")
else:
    print(" Wrong Email ")


