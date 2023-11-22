import requests
from bs4 import BeautifulSoup
import time, random
from urllib.parse import urlparse, parse_qs
import re
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.amazon.de/sp?language=de_DE&ie=UTF8&seller=A2P2JN1SD7RV9V&asin=B085HYVNKX&ref_=dp_merchant_link")
jquery_script = "var script = document.createElement('script'); script.src = 'https://code.jquery.com/jquery-3.6.0.min.js'; document.head.appendChild(script);"
driver.execute_script(jquery_script)
print(jquery_script)
time.sleep(5)
jquery_code = "$('#sp-cc-rejectall-link')[0].click()" 
driver.execute_script(jquery_code)
print("continue without cookies>>>>>>>>")
time.sleep(5)

jquery_code = "$('#spp-expander-about-seller div:last-of-type span a')[0].click()" 
driver.execute_script(jquery_code)
print("view more>>>>>>>>")
time.sleep(5)    
about_info = driver.execute_script("return $('#spp-expander-about-seller div')[0].innerText")
print("notes1:", about_info)
        
# amtsgericht
match1 = re.search(r'Handelsregister: (.+)', about_info)
match2 = re.search(r'Handelsregister (.+)', about_info)
match3 = re.search(r'Registergericht: (.+)', about_info)
        
if match1:
    amtsgericht = match1.group(1)
elif match2:
    amtsgericht = match2.group(1)
elif match3:
    match3_n = re.search(r'Registernummer: (.+)', about_info)
    if match3_n:
        amtsgericht = match3.group(1) +' ' +match3_n.group(1)
    else:
        amtsgericht = match3.group(1)
else:
    amtsgericht = ''       
print("amtsgericht:", amtsgericht)
    
time.sleep(1000)
    
    
    
    