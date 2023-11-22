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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PATH = ChromeDriverManager("116.0.5845.180").install()
service = Service(PATH)
driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome()
actions = ActionChains(driver)
url = 'http://www.importdistribution.be/fr'
driver.get(url)

User = 'salmon.x@mobidecojardin.fr'
mykey = 'DANTIN'
# wait = WebDriverWait(driver, 5)
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cta-login.collapsed')))
# element.click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login-block.fade.in")))
htmltxt = driver.page_source
#print(htmltxt)
element = driver.find_element(By.CSS_SELECTOR, ".login-block.fade.in").find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-loader.btn-danger")

element.click()
wait = WebDriverWait(driver, 10000)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login-block.fade.in")))

htmltxt = driver.page_source



time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '#login').send_keys(User)
driver.find_element(By.CSS_SELECTOR, '#password').send_keys(mykey)
driver.find_element(By.CSS_SELECTOR, '#login_form .btn-danger').click()
time.sleep(1)

results = []
tout = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]    
while True:
    for one in tout:
        try:
            time.sleep(1)
            driver.find_elements(By.CSS_SELECTOR, '.btn-filter')[one].click()
            for i in range(250):
                try:
                    actions.send_keys(Keys.ARROW_DOWN).perform()
                    time.sleep(1)
                except:
                    break
            time.sleep(1)
            Category = driver.find_elements(By.CSS_SELECTOR, '.btn-filter')[one].text
            elements = driver.find_elements(By.CSS_SELECTOR, '#og-grid li')
            print(len(elements))
            for az in elements:
                try:
                    Name = az.find_element(By.CSS_SELECTOR, '.product-desc').text
                    reference = az.find_element(By.CSS_SELECTOR, '.product ').get_attribute('data-product')
                    linc = az.find_element(By.CSS_SELECTOR, '.product').get_attribute('href')
                    img = az.find_element(By.CSS_SELECTOR, '.product .img-responsive').get_attribute('src')
                    price = az.find_element(By.CSS_SELECTOR, '.list-form-line .price').text
                    
                    az.find_element(By.CSS_SELECTOR, '#og-grid .img-responsive').click()
                    time.sleep(2)
                    driver.find_elements(By.CSS_SELECTOR, '.tabs')[1].click()
                    Code_EAN = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(12) > td:nth-child(1) > img').get_attribute('alt')
                    a = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(1) > td:nth-child(1)').text
                    b = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(1) > td:nth-child(2)').text
                    c = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(1) > td:nth-child(3)').text
                    d = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(1) > td:nth-child(4)').text
                    e = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(1) > td:nth-child(5)').text
                    FF = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(2) > td:nth-child(1)').text
                    JJ = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(2) > td:nth-child(2)').text
                    HH = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(2) > td:nth-child(3)').text
                    II = driver.find_element(By.CSS_SELECTOR, '#fiche > div > table > tbody > tr:nth-child(2) > td:nth-child(4)').text
                    tech = a+', ' + b+', ' + c+ 'cm' +', '+ d+', ' + e +'kg'+ '\n' +', ' + FF+', ' + JJ+ 'cm' +', '+ HH+', ' + II +'kg'
                    driver.find_element(By.CSS_SELECTOR, '.og-close').click()
                    time.sleep(1)
                    
                    data = {'Category': Category, 'Name': Name, 'Link': linc, 'Price': price, 'Reference': reference, 'EAN code': Code_EAN, 'Tech': tech, 'image' :img}
                    results.append(data)
                    print(data)
                    print('==================================================')
                except:
                    continue
                keys = results[0].keys()
                with open('importdistributionl.csv', 'w', newline='', encoding="utf-8") as output_file:
                    dict_writer = csv.DictWriter(output_file, keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(results)
        except:
            continue
