from asyncio.windows_events import CONNECT_PIPE_INIT_DELAY
# from asyncio import CONNECT_PIPE_INIT_DELAY
from os import link
from re import X
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import csv
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import threading



import requests
import concurrent.futures

starturl = "https://apps.calbar.ca.gov/attorney/Licensee/Detail/"

def scrape_data(uid):
    current_url = starturl + str(uid)
    response = requests.get(current_url)
    print(current_url)
    if response.status_code == 200:
        print(uid)
    else:
        print("Request failed with status code:", response.status_code)

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit scraping tasks to the executor
        for uid in range(30922, 30930):
            executor.submit(scrape_data, uid)
