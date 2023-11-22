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


# Create a new Chrome browser instance
driver = webdriver.Chrome()
actions = ActionChains(driver)
url = 'https://apps.calbar.ca.gov/attorney/LicenseeSearch/QuickSearch#searchlink'
driver.get(url)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[0])
wait = WebDriverWait(driver, 5, 0.5, TimeoutException)

wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p a strong")))
element = driver.find_element(By.CSS_SELECTOR, "p a strong")
element.click()
time.sleep(1)

results = []
alphaset = ["a","b","c","d","e","f","g","h","i","j","k", "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for alpha in alphaset:
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "p a strong")))
    element = driver.find_element(By.CSS_SELECTOR, "p a strong")

    try:
        actions.move_to_element(element).click().perform()
    except:
        driver.execute_script("arguments[0].scrollIntoView();", element)
        actions.move_to_element(element).click().perform()
    time.sleep(1)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#LastName")))
    element = driver.find_element(By.CSS_SELECTOR, "#LastName")
    element.clear()
    element.send_keys(alpha)
    
    element = driver.find_element(By.CSS_SELECTOR, "#advSearch")
    element.click()

    for i in range(10):
        time.sleep(1)
        trs = driver.find_elements(By.CSS_SELECTOR, ".rowASRLodd")
        for _tr in trs:
            tds = _tr.find_elements(By.CSS_SELECTOR, "td")

            LastName = tds[0].find_element(By.CSS_SELECTOR, "a").text
            Status = tds[1].text
            Number = tds[2].text
            City = tds[3].text
            AdmissionDate = tds[4].text
            addinfo = "-"
            phone_fax = "-"
            email_site = "-"

            linc = tds[0].find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(linc)
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(1)")))
                addinfo = driver.find_element(By.CSS_SELECTOR, "#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(1)").text
            
                # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(2)")))
                phone_fax = driver.find_element(By.CSS_SELECTOR, "#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(2)").text
            
                # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(3)")))
                email_site = driver.find_element(By.CSS_SELECTOR, "#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(3)").text
            except TimeoutException as e:
                pass
            driver.switch_to.window(driver.window_handles[0])

            # time.sleep(1)
            rowdata = {'LastName':LastName,'Status':Status,'Number':Number,'City':City,'AdmissionDate':AdmissionDate,'Address':addinfo,'Phone&Fax':phone_fax,'Email&Website':email_site,'Link':linc}
            results.append(rowdata)

            keys = results[0].keys()
            with open('output2.csv', 'w', newline='', encoding="utf-8") as output_file:
                dict_writer = csv.DictWriter(output_file, keys)
                dict_writer.writeheader()
                dict_writer.writerows(results)
        
        # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.paginate_button.next.disabled")))
        disbtn = driver.find_elements(By.CSS_SELECTOR, "a.paginate_button.next.disabled")
        print(len(disbtn))
        if len(disbtn) > 0: 
            break
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.paginate_button.next")))
        element = driver.find_element(By.CSS_SELECTOR, "a.paginate_button.next")
        actions.move_to_element(element).click().perform()
        

time.sleep(50)




