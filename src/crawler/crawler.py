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
from utils.crawler_utils import open_selenium_remote_browser, get_level_1, get_level_2
from utils.ETL_utils import save_data_to_json

### Open Chrome WebDriver
def main():
    url = 'https://sinica.digitalarchives.tw/collection.php?type=3799'  # URL of the Academia Sinica Digital Archive Website
    driver = open_selenium_remote_browser(url)  # Initialize and open a remote browser 

    # Use the get_level_1 function to collect links
    links_list = get_level_1(driver)
    all_data = []

    for link in links_list:
        data = get_level_2(driver, link)
        all_data.append(data)
    
    save_data_to_json(all_data)
        
    driver.quit()  # Close the browser session and quit the driver

if __name__ == "__main__":
    main()  # Execute the main function if this script is run as the main program
