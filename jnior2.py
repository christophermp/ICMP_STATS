import json
import urllib.request
import threading
import time
status_url = "http://10.0.0.111:8080/getStatus"
device_url = "http://10.0.0.111:8080/getDevice"
temp_url = "http://10.0.0.111:8080/getdevice?device=type28_1"

class readDevice(adress):
        urlData = adress
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        statusData = json.loads(data.decode(encoding))
        resp_dict = statusData
        return resp_dict

#****************************************************************#
    
stats = readDevice(status_url)

hostname = stats['Hostname']
ipAdress = stats['IpAddress']
model = stats['Model']
serial = stats['SerialNumber']
janosSw = stats['JANOSVersion']
cinemaSw = stats['CinemaVersion']
UptimeSec = stats['UptimeSeconds']
UptimeDay = stats['UptimeString']
#print(hostname, ipAdress, model, serial, janosSw, cinemaSw,UptimeDay,UptimeSec)

#****************************************************************#

temp = fetchData(temp_url)

Temprature = temp['Celsius']
print("Tempraturen er: ", Temprature)

#****************************************************************#

device = fetchData(device_url)

din1 = device['DIN1']
din2 = device['DIN2']
din3 = device['DIN3']
din4 = device['DIN4']
rout1 = device['ROUT1']
rout2 = device['ROUT2']
rout3 = device['ROUT3']
rout4 = device['ROUT4']
rout5 = device['ROUT5']
rout6 = device['ROUT6']
rout7 = device['ROUT7']
rout8 = device['ROUT8']
rout9 = device['ROUT9']
rout10 = device['ROUT10']
rout11 = device['ROUT11']
rout12 = device['ROUT12']
rout13 = device['ROUT13']
rout14 = device['ROUT14']
rout15 = device['ROUT15']
rout16 = device['ROUT16']

    #Inputs
if rout1 == True:
    print("Output 1 is live")
elif rout1 == False:
    print("Output 1 is closed")
if rout2 == True:
    print("Output 2 is live")
elif rout2 == False:
    print("Output 2 is closed")
if rout3 == True:
    print("Output 3 is live")
elif rout3 == False:
    print("Output 3 is closed")
if rout4 == True:
    print("Output 4 is live")
elif rout4 == False:
    print("Output 4 is closed")
if rout5 == True:
    print("Output 5 is live")
elif rout5 == False:
    print("Output 5 is closed")
if rout6 == True:
    print("Output 6 is live")
elif rout6 == False:
    print("Output 6 is closed")
if rout7 == True:
    print("Output 7 is live")
elif rout7 == False:
    print("Output 7 is closed")
if rout8 == True:
    print("Output 8 is live")
elif rout8 == False:
    print("Output 8 is closed")
if rout9 == True:
    print("Output 9 is live")
elif rout9 == False:
    print("Output 9 is closed")
if rout10 == True:
    print("Output 10 is live")
elif rout10 == False:
    print("Output 10 is closed")
if rout11 == True:
    print("Output 11 is live")
elif rout11 == False:
    print("Output 11 is closed")
if rout12 == True:
    print("Output 12 is live")
elif rout12 == False:
    print("Output 12 is closed")
if rout13 == True:
    print("Output 13 is live")
elif rout5 == False:
    print("Output 13 is closed")