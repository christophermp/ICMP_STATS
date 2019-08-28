import os
from datetime import time
import time
import dataCollector as dc

#Om det er Atmos må man legge til parameter True
def start():
    print("Starter Sal 2")
    dc.dataFetcher('10.10.97.2', True)
    time.sleep(60)
    print("Starter Sal 3")
    dc.dataFetcher('10.6.98.2', True)
    time.sleep(60)
    print("Starter Sal 4")
    dc.dataFetcher('10.10.99.2', True)
    time.sleep(60)
    print("Starter Sal 5")
    dc.dataFetcher('10.10.100.2', True)
    time.sleep(60)
    print("Starter Sal 6")
    dc.dataFetcher('10.10.101.2', True)
    time.sleep(60)
    print("Starter Sal 7")
    dc.dataFetcher('10.10.102.2', True)
    time.sleep(60)
    print("Starter Sal 8")
    dc.dataFetcher('10.10.103.2', True)
    time.sleep(60)
    print("Starter Sal 9")
    dc.dataFetcher('10.10.104.2', True)
    time.sleep(60)
    print("Starter Sal 10")
    dc.dataFetcher('10.10.105.2', True)
    time.sleep(60)
    print("Starter Sal 11")
    dc.dataFetcher('10.10.106.2', True)
    time.sleep(60)
    print("Starter Sal 12")
    dc.dataFetcher('10.10.107.2', True)
    time.sleep(60)
    print("Starter Sal 13")
    dc.dataFetcher('10.10.108.2', True)
    time.sleep(60)
    print("Starter Sal 14")
    dc.dataFetcher('10.10.109.2', True)

def executeSomething():
    #Fra it trigger readAndInsert
    start()
    #Bekreftelse på skript utført
    counter = 1
    print(f"Venter 5min Antall ganger kjørt{counter}")
    #Timer på 300 = 5min Det ser ut til at det er bare 30sek som fungerer..
    time.sleep(300)

while True:
    executeSomething()
