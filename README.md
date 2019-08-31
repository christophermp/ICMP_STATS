# BARCO ICMP MESSAGE READER
This is a monitoring tool for your ICMP`s. (BIMR)

![alt text](https://github.com/christophermp/ICMP_STATS/raw/master/images/Skjermbilde.PNG)




## Prerequisites
-Windows, MAC or Linux x86/64
-Python 3.6 or higher.
-Know how to create batch files.
-Gekko(firefox) or Chromedriver (Follows the download)

## Installation

Be sure to have python installed. Works on Python 3.7
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install BIMR.

```bash
pip install -r requirements.txt
```

## Usage

Run the functions induvidualy:

Trigger:
```python
import trigger

trigger.executeSomething() # Starts the collection of data
```
Web-Server:
```python
import trigger

trigger.app() # Starts the Web-Server
```

It`s not recommended to run them this way. The recommended way is:
-Dubble click on triggers.py
-Dubble click on main.py

Don`t close the console Windows. If so the services will stop.

## ATMOS

If there is **ATMOS** present be **SURE** to add **True** after ip in **trigger.py**.
If there is **CP650 / CP750** or other analog audio devices set it to **False**

## Initial Setup

trigger.py
```python
#Edit ip`s for your own servers.
#Set parameter as True if there is ATMOS present, Else set False
    print("Starting Screen 1")
    dc.dataFetcher('10.10.97.2', True)
    time.sleep(60)
    print("Starting Screen 2")
    dc.dataFetcher('10.6.98.2', True)
    time.sleep(60)
#ECT...
```
Be sure to remove or add screens that aren`t present

main.py
```python
#Add or remove amout of screens
    screen1 =[]
    screen2 =[]
    screen3 =[]
    screen4 =[]
    screen5 =[]
    screen6 =[]
    screen7 =[]

#Then edit amount of while statements
#Be sere to name the json file exactly as the servers screen name!
    with open('static/data/Screen1.json', 'r') as f:
        screen1 = json.load(f)
        f.close()
    with open('static/data/Screen2.json', 'r') as f:
        screen2 = json.load(f)
        f.close()

#Then edit amounts of return fields:
return data2=screen2, data3=screen3, data4=screen4, data5=screen5, data6=screen6, data7=screen7 #ECT...
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
