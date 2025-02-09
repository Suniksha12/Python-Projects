#importing module
import datetime
import time

end_time = datetime.datetime(2025,02,09)
site_block = ["github.com/Suniksha12","www.linkedin.com/feed/"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

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