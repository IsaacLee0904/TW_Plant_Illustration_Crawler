### import package
import datetime
from time import sleep
import sys
import re
## web crawling with Selenium
# basic selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

### open chrome webdriver
driver = webdriver.Remote(
        command_executor = 'http://172.17.0.2:4444/wd/hub' # selnium docker cotainer IPAdress
        , desired_capabilities = DesiredCapabilities.CHROME
)
driver.get('https://sinica.digitalarchives.tw/collection.php?type=3799') # Academia Sinica Digital Archive Website
print(driver.title)
driver.quit() 