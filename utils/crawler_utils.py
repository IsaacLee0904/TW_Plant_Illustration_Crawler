### import package
import datetime
from time import sleep
import sys
import json
### web crawling with Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

def open_selenium_remote_browser(url):
    """
    Initializes a remote Selenium WebDriver session and navigates to the specified URL.
    
    Args:
        url (str): The URL to be visited.
        
    Returns:
        webdriver.Remote: An instance of the remote WebDriver.
    """
    # Initialize the remote WebDriver with the specified Selenium Grid server address
    # and desired browser capabilities for Chrome.
    driver = webdriver.Remote(
        command_executor='http://172.17.0.2:4444/wd/hub',  # Selenium Docker container IP address
        desired_capabilities=DesiredCapabilities.CHROME
    )
    
    # Navigate to the specified URL using the WebDriver.
    driver.get(url)
    
    return driver

def get_level_1(driver, max_pages=4924):
    """
    Collects links from all pages by iterating through pages and clicking the "next page" button until it no longer exists
    or the specified maximum number of pages has been reached.
    
    Args:
        driver (webdriver.Remote): The Selenium WebDriver instance.
        max_pages (int): The maximum number of pages to iterate through. Defaults to 5.
        
    Returns:
        list: A list of collected links.
    """
    
    links_list = []  # Corrected variable name
    current_page = 1  # Initialize current page counter

    while True:
        # Collect all links on the current page
        page_links = driver.find_elements(By.XPATH, '//*[@id="list"]/li/div[2]/a')
        for link in page_links:
            links_list.append(link.get_attribute('href'))  # Corrected variable name
        
        # Check if the current page count exceeds the max_pages limit
        if current_page >= max_pages:
            break  # Exit the loop if the maximum number of pages has been reached
        
        # Try to find and click the "next page" button
        try:
            next_page_button = driver.find_element(By.XPATH, '//*[@id="main-content-inner"]/div[3]/div[4]/a/i')
            next_page_button.click()
            sleep(2)  # Wait for the page to load after clicking
            current_page += 1  # Increment the current page counter after successfully navigating to the next page
        except Exception as e:
            break  # Break the loop if "next page" button is not found

    return links_list

def get_text_info(driver, xpath):
    """
    Safely finds an element by its XPath, returning None if the element does not exist.
    
    Args:
        driver (webdriver.Remote): The Selenium WebDriver instance.
        xpath (str): The XPath of the element to find.
    
    Returns:
        str: The text of the found element or "NULL" if not found.
    """
    try:
        return driver.find_element(By.XPATH, xpath).text

    except NoSuchElementException:
        return "NULL"  # return NULL if element does not exist

def get_image_url(driver, xpath):
    """
    Safely finds an image element by its XPath and returns its 'src' attribute.
    
    Args:
        driver (webdriver.Remote): The Selenium WebDriver instance.
        xpath (str): The XPath of the image element to find.
    
    Returns:
        str: The 'src' attribute of the found image element or "NULL" if not found.
    """
    try:
        image_element = driver.find_element(By.XPATH, xpath)
        return image_element.get_attribute('src')

    except NoSuchElementException:
        return "NULL" # return NULL if element does not exist

def get_level_2(driver, url):
    """
    Navigates to the given URL and extracts specified information from the page.
    
    Args:
        driver (webdriver.Remote): The Selenium WebDriver instance.
        url (str): URL of the page to extract information from.
        
    Returns:
        dict: Extracted information in a dictionary.
    """
    driver.get(url)

    data = {
        "chinese_name": get_text_info(driver, '//*[@id="collection-title"]/dd[1]'),
        "scientific_name": get_text_info(driver, '//*[@id="collection-title"]/dd[2]'),
        "museum_number": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[1]'),
        "catalog_number": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[2]'),
        "reference": get_text_info(driver, '//*[@id="quote-data"]'),
        "collection_date": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[17]'),
        "collector_chinese": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[15]'),
        "collector_Eng": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[16]'),
        "latitude": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[20]'),
        "longitude": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[21]'),
        "country": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[22]'),
        "administrative_region": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[23]'),
        "minimum_elevation": get_text_info(driver, '//*[@id="main-content-inner"]/article/dl/dd[24]'),
        "image_url": get_image_url(driver, '//*[@id="main-content-inner"]/article/div/div[2]/div/img'),
    }
    
    return data