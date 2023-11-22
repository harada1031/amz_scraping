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
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from amazoncaptcha import AmazonCaptcha
from selenium.webdriver.chrome.options import Options
import seller
import product
import mydb

# db connection
try:
    # db = mydb.db_connect("localhost", 3306, "root","","amz") #local
    db = mydb.db_connect("91.107.206.223", 3308, "ihor_user","eCZ5xmpfNf6lZ+Ti7N9Eih6D5r8RV9Cm5D+69DkM0VE=","ihor_grap") #online
except Exception as db_error:
    print(db_error)
    exit()
print("Connected to database.........")

# chrome driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5, 0.5, TimeoutException)
actions = ActionChains(driver)


url = 'https://www.amazon.de/dp/B097TTLDSP/ref=sspa_dk_detail_0?pf_rd_p=ae2317a0-2175-4285-af64-66539858231f&pf_rd_r=3DTVE93WZ4VWH9TNR3P4&pd_rd_wg=z3NVG&pd_rd_w=FdyMs&content-id=amzn1.sym.ae2317a0-2175-4285-af64-66539858231f&pd_rd_r=2e780df6-7700-47d0-b4b4-1822c02be39b&s=drugstore&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw&th=1'
driver.get(url)
driver.execute_script("window.open('');")
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
time.sleep(7)



# captcha solving #############################################################################################################
# captcha = AmazonCaptcha.fromdriver(driver)
# while True:
#     captcha = AmazonCaptcha.fromdriver(driver)
#     solution = captcha.solve()
#     print(solution)
#     time.sleep(3)
#     captcha_input = driver.find_element(By.CSS_SELECTOR, "#captchacharacters")
#     captcha_input.clear()
#     time.sleep(3)
#     captcha_input.send_keys(solution)
#     time.sleep(2)
#     captcha_btn = driver.find_element(By.CSS_SELECTOR, "button.a-button-text")
#     captcha_btn.click()
#     if solution != 'Not solved':
#         break

# getin url and change location ###############################################################################################
jquery_script = "var script = document.createElement('script'); script.src = 'https://code.jquery.com/jquery-3.6.0.min.js'; document.head.appendChild(script);"
driver.execute_script(jquery_script)
print(jquery_script)
time.sleep(5)
try:
    jquery_code = "$('#sp-cc-rejectall-link')[0].click()" 
    driver.execute_script(jquery_code)
    print("continue without cookies>>>>>>>>")
    time.sleep(5)
    jquery_code = "$('#nav-global-location-popover-link')[0].click()" 
    driver.execute_script(jquery_code)
    print("deliver>>>")
    time.sleep(2)
    post_input = driver.find_element(By.CSS_SELECTOR, "#GLUXZipUpdateInput")
    post_input.clear()
    time.sleep(1)
    post_input.send_keys('25885')
    print('postcode>>>>>>>>')
    time.sleep(2)
    jquery_code = "$('#GLUXZipUpdate-announce').click()" 
    driver.execute_script(jquery_code)
    print("apply>>>>>")
    time.sleep(2)
    jquery_code = "$('#GLUXConfirmClose').click()" 
    driver.execute_script(jquery_code)
    print('continue>>>>>>>>>')
    driver.refresh()
    time.sleep(2)
except Exception as e:
    print("url to location change :::::",e)
    pass    

# get seller data #################################################################################################################################
################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

# links = []
# seller_link = driver.find_element(By.CSS_SELECTOR, "#sellerProfileTriggerId").get_attribute("href")
# print(seller_link)
# seller.get_seller(seller_link)

# # get related products url ###
# ldiv_index = ['1','4','2']
# print("--------------------------------")
# for div_i in ldiv_index:
#     div_css = "#anonCarousel" + str(div_i)
#     while True:
#         ldiv = driver.find_elements(By.CSS_SELECTOR, div_css)
#         if len(ldiv)>0:
#             break
#         actions.send_keys(Keys.PAGE_DOWN).perform()
#         time.sleep(1)
#     link1 = ldiv[0].find_element(By.CSS_SELECTOR, "ol li:nth-of-type(1) div a.a-link-normal").get_attribute("href")
#     link2 = ldiv[0].find_element(By.CSS_SELECTOR, "ol li:nth-of-type(2) div a.a-link-normal").get_attribute("href")
#     link3 = ldiv[0].find_element(By.CSS_SELECTOR, "ol li:nth-of-type(3) div a.a-link-normal").get_attribute("href")
#     print(link1, link2, link3)
#     links.append(link1)
#     links.append(link2)
#     links.append(link3)

# # save data to mysql table ###
# for linc in links:
#     num = mydb.is_link_used(db, linc)
#     if num <1:
#         mydb.insert_link(db,linc)
#     else:
#         print("this url is already used")
        

################################################################################################################
####################################################################################################################
product.get_products(driver, db, url)
    
mydb.db_close(db)
# Close the web driver
time.sleep(1000)


