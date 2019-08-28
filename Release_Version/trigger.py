import os
from datetime import time
import time
import dataCollector as dc

def start():
    print("Starter Sal 2")
    dc.dataFetcher('10.10.97.2')
    time.sleep(60)
    print("Starter Sal 3")
    dc.dataFetcher('10.6.98.2')
    time.sleep(60)
    dc.dataFetcher('10.10.99.2')
    time.sleep(60)
    dc.dataFetcher('10.10.100.2')
    time.sleep(60)
    dc.dataFetcher('10.10.101.2')
    time.sleep(60)
    dc.dataFetcher('10.10.102.2')
    time.sleep(60)
    dc.dataFetcher('10.10.103.2')
    time.sleep(60)
    dc.dataFetcher('10.10.104.2')
    time.sleep(60)
    dc.dataFetcher('10.10.105.2')
    time.sleep(60)
    dc.dataFetcher('10.10.106.2')
    time.sleep(60)
    dc.dataFetcher('10.10.107.2')
    time.sleep(60)
    dc.dataFetcher('10.10.108.2')
    time.sleep(60)
    dc.dataFetcher('10.10.109.2')

def executeSomething():
    #Fra it trigger readAndInsert
    start()
    #Bekreftelse på skript utført
    count = 0
    counter = count +1 
    print(f"Venter 5min Antall ganger kjørt{counter}")
    #Timer på 300 = 5min Det ser ut til at det er bare 30sek som fungerer..
    time.sleep(30)

while True:
    executeSomething()
