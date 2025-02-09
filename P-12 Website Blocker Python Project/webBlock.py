#importing module
import datetime
import time

end_time = datetime.datetime(2025,02,09)
site_block = ["",""] # give the links of the webiste to be blocked.
host_path = "" # give your hoste file path 
redirect = "" # give your network address

while True:
    if datetime.datetime.now()<end_time:
        print("start Blocking")
        #we will use file handling 
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write( redirect + " " + website + "\n")
                else:
                    pass
    else:
        with open(host_path,"r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)

            #then convert it into a irginal file using truncate function
            host_file.truncate()

        #we will use sleep function which gives delay
        time.sleep(5)

#if you want to run the file then open the command prompt in the same directory where your program file is located
#make sure you open it with open with administrators perminisions

"""And if want to immediately unblock your website
then open your host file and then you will see 2 website that are blocked 
you can remove it from there as well as in your python file you can comment out 
from the  if datetime.datetime.now()<end_time:
        print("start Blocking")
        #we will use file handling 
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write( redirect + " " + website + "\n")
                else:
                    pass
    else: commenet this code and your webiste will be unblocked."""