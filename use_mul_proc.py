import multiprocessing
from multiprocessing import Pool
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

import requests
from bs4 import BeautifulSoup


num_cores = multiprocessing.cpu_count()

print(f"Number of CPU cores: {num_cores}")


# Create a new Chrome browser instance


def scrape_data(alpha):
    print(alpha, alpha+1)    
        
args_list = [(alpha) for alpha in range(0,2)]

def process_task(args):
    alpha = args
    return scrape_data(alpha)
pool = multiprocessing.Pool()

results = pool.map(process_task, args_list)

for result in results:
    # Process each result
    print(results)

time.sleep()