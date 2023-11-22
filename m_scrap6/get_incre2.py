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
chrome_options = Options()
chrome_options.add_argument("--headless")

# Create the driver with the options
driver = webdriver.Chrome(options=chrome_options)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 3, 0.3, TimeoutException)

starturl="https://apps.calbar.ca.gov/attorney/LicenseeSearch/AdvancedSearch?LastNameOption=b&MiddleNameOption=b&MiddleName=&FirmNameOption=b&FirmName=&CityOption=b&City=&State=&Zip=&District=&County=&LegalSpecialty=&LanguageSpoken=&PracticeArea="
endurl="&LastName=b&FirstNameOption=b&FirstName=b"

headers = ['LastName','Status','Number','City','AdmissionDate','Address','Phone','Fax','Email','Website','Speciality','Link']

alphaset = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
falphaset = ["a","b","c","d","e","f","g","h","i","j","k", "l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


for alpha in alphaset[4:8]:
    
    for falpha in falphaset:
        results = []
        currenturl = starturl+"&LastName="+alpha+"&FirstNameOption=b&FirstName="+falpha
        print("================================")
        print(currenturl)
        driver.get(currenturl)
        # start search
        dataexist = True
        table = driver.find_elements(By.CSS_SELECTOR, "#tblAttorney")
        if len(table) == 0:
            dataexist = False

        while dataexist == True:
            time.sleep(1)
            trs = driver.find_elements(By.CSS_SELECTOR, ".rowASRLodd")
            if len(trs) == 0:
                break
            for _tr in trs:
                tds = _tr.find_elements(By.CSS_SELECTOR, "td")

                LastName = tds[0].find_element(By.CSS_SELECTOR, "a").text
                Status = tds[1].text
                Number = tds[2].text
                City = tds[3].text
                AdmissionDate = tds[4].text
                addinfo = "-"
                phone = "-"
                fax = "-"
                email="-"
                site = "-"

                linc = tds[0].find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                
                ## send request
                response = requests.get(linc)
                
                if response.status_code == 200:
                    # Parse the HTML content using BeautifulSoup
                    soup = BeautifulSoup(response.content, "html.parser")
                    
                    # Find specific HTML elements using CSS selectors
                    addinfo_ele = soup.select_one("#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(1)")
                    if addinfo_ele:
                        addinfo_mul = addinfo_ele.get_text().strip().split("Address:")
                        if len(addinfo_mul) >1:
                            addinfo=addinfo_mul[1]
                    
                    p_f = soup.select_one("#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(2)")
                    if p_f:
                        phone = p_f.get_text().strip().split("Phone: ")[1].split(" | ")[0].split()[0]
                        fax = p_f.get_text().strip().split("Fax: ")[1]

                    email_site = soup.select_one("#moduleMemberDetail > div:nth-of-type(3) > p:nth-of-type(3)")
                    if email_site:               
                        p_element = soup.find('p', class_='donotprint')
                        style_element = p_element.find_next_sibling('style')
                        style_content = style_element.string
                        span_elements = email_site.find_all('span')
                        
                        for span_element in span_elements:
                            span_id = span_element.get('id')
                            css_selector = f'#{span_id}{{display:inline;}}'
                            
                            if css_selector in style_content:
                                email = span_element.text
                                break
                        site = email_site.get_text().strip().split("Website:")[1].split()[0]
                    
                else:
                    print("Request failed with status code:", response.status_code)
                ## end request

                # # go second tab 
                
                # # leave second tab

                rowdata = {'LastName':LastName,'Status':Status,'Number':Number,'City':City,'AdmissionDate':AdmissionDate,'Address':addinfo,'Phone':phone,'Fax':fax,'Email':email,'Website':site,'Speciality':'Have not Cert.Legal Specialty','Link':linc}
                results.append(rowdata)
            try:
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.paginate_button.next.disabled")))
            except Exception as e:
                print("+50 to memory")
                actions.send_keys(Keys.PAGE_UP).perform()
                pass
            disbtn = driver.find_elements(By.CSS_SELECTOR, "a.paginate_button.next.disabled")
            # print(len(disbtn))
            if len(disbtn) > 0: 
                break

            # wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.paginate_button.next")))
            else:
                jquery_code = "$('#tblAttorney_next').click()"  # Replace "selector" and "yourFunction()" with the actual jQuery selector and function you want to run
                driver.execute_script(jquery_code)
                # try:
                #     wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.paginate_button.next")))
                # except Exception:
                #     actions.send_keys(Keys.PAGE_UP).perform()
                #     pass
                # try:
                #     element = driver.find_element(By.CSS_SELECTOR, "a.paginate_button.next")
                #     actions.move_to_element(element).click().perform()
                # except Exception:
                #     actions.send_keys(Keys.PAGE_UP).perform()
                #     element = driver.find_element(By.CSS_SELECTOR, "a.paginate_button.next")
                #     actions.move_to_element(element).click().perform()
                #     pass

        # end search
       
        with open('output.csv', 'a', newline='', encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, headers)
            dict_writer.writerows(results)           
            print("added file from memory")

print("finish no_cre 2****************************************************************")
time.sleep(20)




