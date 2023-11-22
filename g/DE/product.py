from asyncio.windows_events import CONNECT_PIPE_INIT_DELAY
from os import link
from re import X
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
from urllib.parse import urlparse, parse_qs
import sellertab
import mydb

def get_products(driver, db, url):
    actions = ActionChains(driver)
    driver.get(url)
    time.sleep(random.randint(55, 165))
    links = []
    try:
        seller_link = driver.find_element(By.CSS_SELECTOR, "#sellerProfileTriggerId").get_attribute("href")
        print(seller_link)
        
        parsed_url = urlparse(seller_link)
        query_params = parse_qs(parsed_url.query)
        seller_id = query_params.get('seller')[0]
        print("seller_id",seller_id)
        
        num = mydb.is_sellerid_exist(db, seller_id)
        if num <1:
            data = sellertab.get_seller(driver, seller_link)
            if data is not None:
                mydb.insert_sellerinfo(db, data)
        else:
            print("Seller info already exists")
    except Exception as e:
        print("Seller link not exists",e)
        pass
    driver.switch_to.window(driver.window_handles[0])


    # get related products url
    ldiv_index = ['1','2','3','4','5']
    print("--------------------------------")
    for div_i in ldiv_index:
        div_css = "#anonCarousel" + str(div_i)
        print("div_i:",div_i)
        while True:
            ldiv = driver.find_elements(By.CSS_SELECTOR, div_css)
            if len(ldiv)>0:
                break
            scroll_pos = driver.execute_script('return window.scrollY')
            print(scroll_pos)
            actions.send_keys(Keys.PAGE_DOWN).perform()
            time.sleep(1)
            new_scroll_pos = driver.execute_script('return window.scrollY')
            if scroll_pos == new_scroll_pos:
                print("end of page >>>>>>>>>>>")
                actions.send_keys(Keys.HOME).perform()
                break
            time.sleep(1)
        try:
            link1 = ldiv[0].find_element(By.CSS_SELECTOR, "ol li:nth-of-type(1) div a.a-link-normal").get_attribute("href")
            link2 = ldiv[0].find_element(By.CSS_SELECTOR, "ol li:nth-of-type(2) div a.a-link-normal").get_attribute("href")
            link3 = ldiv[0].find_element(By.CSS_SELECTOR, "ol li:nth-of-type(3) div a.a-link-normal").get_attribute("href")
            # print(link1, link2, link3)
            links.append(link1)
            links.append(link2)
            links.append(link3)
        except Exception as e:
            print("not found")
            pass
    print("length of product url:",len(links))
    if len(links) > 0:        
        for linc in links:
            num = mydb.is_already_added(db, linc)
            print("num",num)
            if num <1 and linc.find("aax-eu.amazon.de") == -1:
                mydb.insert_link(db,linc)
                time.sleep(0.5)
            else:
                print("this product url is already used >>>>>")
    mydb.update_link(db, url)
    
    next_url = mydb.next_link(db)
    print(next_url)
    # get_products(driver, db, next_url) 
    
    return next_url
    



