### import package
import os
import datetime
from time import sleep
import sys
import re
### web crawling with Selenium
from selenium.webdriver.common.by import By

### import modules
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from utils.crawler_utils import open_selenium_remote_browser
from utils.crawler_utils import get_level_1

### Open Chrome WebDriver
def main():
    url = 'https://sinica.digitalarchives.tw/collection.php?type=3799'  # URL of the Academia Sinica Digital Archive Website
    driver = open_selenium_remote_browser(url)  # Initialize and open a remote browser 

    # Use the get_level_1 function to collect links
    links_list = get_level_1(driver)

    # Print the collected links
    for link in links_list:
        print(link)
        
    driver.quit()  # Close the browser session and quit the driver

if __name__ == "__main__":
    main()  # Execute the main function if this script is run as the main program
