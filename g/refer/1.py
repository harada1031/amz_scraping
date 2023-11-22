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

from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36")

driver = webdriver.Chrome(options=options)




# Open the URL
url = 'https://www.amazon.de/sp?ie=UTF8&seller=A1K6TAQBRYGCP&asin=B097TTLDSP&ref_=dp_merchant_link&isAmazonFulfilled=1'
# url = 'https://www.amazon.de/Innotech-Neurological-Reflexes-Surface-Reactions/dp/B097TTLDSP?ref_=v_sp_product_dpx&th=1'

driver.get(url)

# Perform other actions on the original page
time.sleep(5)
driver.get(url)
time.sleep(5)
driver.get(url)
time.sleep(5)
driver.get(url)
time.sleep(5)
jquery_script = "var script = document.createElement('script'); script.src = 'https://code.jquery.com/jquery-3.6.0.min.js'; document.head.appendChild(script);"
driver.execute_script(jquery_script)
print(jquery_script)
time.sleep(5)
try:
    jquery_code = "$('#sp-cc-rejectall-link')[0].click()" 
    driver.execute_script(jquery_code)
    print("continue without cookies>>>>>>>>")
    driver.execute_script("$('#page-section-detail-seller-info')")
    
    table = driver.find_element(By.CSS_SELECTOR, "#page-section-detail-seller-info")
    print(table.text)
    
    jquery_code = "$('#nav-global-location-slot').click()" 
    driver.execute_script(jquery_code)
    print("deliver>>>")
    time.sleep(2)
    # jquery_code = "$('#GLUXCountryList').value = 'GB'" 
    # driver.execute_script(jquery_code)
    # print("GB>>>>>")
    # time.sleep(2)
    jquery_code = "$('#GLUXCountryListDropdown span.a-button-text.a-declarative').click()" 
    driver.execute_script(jquery_code)
    print("list>>>>>")
    time.sleep(2)
    jquery_code = "$('#GLUXCountryList_226').click()" 
    driver.execute_script(jquery_code)
    print("item>>>>>")
    time.sleep(2)
    jquery_code = "$('button[name=glowDoneButton]').click()" 
    driver.execute_script(jquery_code)
    print('done>>>>>>>>>')
    driver.refresh()
    
    driver.get("https://www.amazon.de/sp?ie=UTF8&seller=A1K6TAQBRYGCP&asin=B097TTLDSP&ref_=dp_merchant_link&isAmazonFulfilled=1#")
except Exception as e:
    print(e.message)
    pass


# Close the web driver
time.sleep(100)

