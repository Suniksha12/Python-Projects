#importing module
import datetime

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
                    host_file.write()
    else:
        pass