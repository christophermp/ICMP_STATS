import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import sys
from datetime import datetime
import json
import sys

#pip install lxml
def dataFetcher(adress):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    #dir = os.path.dirname(__file__)
    chrome_driver_path = "static/drivers/chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)

    ip = adress #'10.10.109.2'

    icmp_URL = "http://" + ip
    driver.get(icmp_URL)


    # login
    print("Logger inn..")
    time.sleep(5)
    try:
        inputElement = driver.find_element_by_id("loginUsername")
        inputElement.send_keys("admin")
    except NoSuchElementException as exception:
        print("Login failed")
        driver.quit()
    inputElement = driver.find_element_by_id("loginPass")
    inputElement.send_keys("Admin1234")
    #inputElement.submit()
    time.sleep(1)
    elem = driver.find_element_by_id("loginSubmit")
    elem.click()
    print("Leser data..")
    time.sleep(6)

    raidStatus = driver.find_elements_by_xpath('//*[@id="raidStatusText"]')
    deviceErrors = driver.find_elements_by_xpath('//*[@id="dashStatus"]/div[3]/div[1]/p[1]')
    deviceWarnings = driver.find_elements_by_xpath('//*[@id="dashStatus"]/div[3]/div[2]/p[1]')
    deviceMaintenance = driver.find_elements_by_xpath('//*[@id="dashStatus"]/div[3]/div[3]/p[1]')
    #Playing Now
    currentlyPlaying = driver.find_elements_by_xpath('//*[@id="dashPlayer"]/div[2]/p[1]')
    currentPosition = driver.find_elements_by_xpath('//*[@id="dashPlayer"]/div[2]/p[3]')

    print("Disk Status: ", raidStatus[0].text)
    print("Kritiske feil: ", deviceErrors[0].text)
    print("Varsler: ", deviceWarnings[0].text)
    print("Vedlikehold: ", deviceMaintenance[0].text)
    #
    print("Viser nå: ", currentlyPlaying[0].text)
    print("Tid Spilt: ", currentPosition[0].text)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    disk = raidStatus[0].text
    critical = deviceErrors[0].text
    warnings = deviceWarnings[0].text
    maint = deviceMaintenance[0].text
    ftrTitle = currentlyPlaying[0].text
    playerState = currentPosition[0].text
    """
    listings = soup.find_all("div")
    listings[:5]
    print(listings)
    """
    readLamp = soup.find('p', attrs={'id':'mslampStatus'})
    lampStatus = readLamp.text
    print(lampStatus)
    readSound = soup.findAll('p',attrs={"class":"msSoundConnectionStatus"})

    def checkSound():
        for x in readSound:
            print("Lydprosesor Status: ", x.find('p').text)
            val = x.find('p').text
            return val

    soundStatus = checkSound()

    driver.get('https://'+ ip +':43744/#sms/monitoring')
    time.sleep(4)
    time.sleep(2)
    soup1 = BeautifulSoup(driver.page_source, 'html.parser')
    messages=driver.find_element_by_id("messages").text
    print(messages)


    screenName = driver.find_element_by_id("msAuditoriumName")
    print("Sal: ", screenName.text)
    screenName2 = screenName.text

    server_values = {'screenName':'No data yet',
                    'lampStatus': 'No data yet',
                    'criticalCount': 0,
                    'maintCount': 0,
                    'messagesInfo': 'No data yet',
                    'diskStatus': 'No data yet',
                    'soundState': 'No data yet',
                    'playerRuntime': 0,
                    'movieTitle': 'No data yet'
                    }

    server_values['screenName'] = screenName2
    server_values['lampStatus'] = lampStatus
    server_values['criticalCount'] = critical
    server_values['errorCount'] = warnings
    server_values['maintCount'] = maint
    server_values['messagesInfo'] = messages
    server_values['diskStatus'] = disk
    server_values['soundState'] = soundStatus
    server_values['playerRuntime'] = playerState
    server_values['movieTitle'] = ftrTitle

    with open(f'static/data/{screenName2}.json', 'w') as file:
        file.write(json.dumps(server_values))
    #screenName2, lampStatus, critical, maint, messages, disk, soundStatus, playerState, ftrTitle

    driver.quit()