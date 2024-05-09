import datetime
import time

end_time = datetime.datetime(2024,10,5)

site_block = ["www.wscubetech.com"]
host_path = "C:/Window/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now()<end_time:
        print("start blocking")
        with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect+" "+website+"\n")
                else:
                    pass

    else:            
        with open(host_path,"r+") as host_file:
            comtent = host_file.readline()
            host_file.seek(0)
            for line in comtent:
                if not any(website in line for website in site_block):
                    host_file.write(line)
            host_file.truncate()

        time.sleep(5)

