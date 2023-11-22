import time
from urllib.parse import urlparse, parse_qs
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random

def get_seller(driver,url):
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url)
    time.sleep(random.randint(55, 165))
    jquery_script = "var script = document.createElement('script'); script.src = 'https://code.jquery.com/jquery-3.6.0.min.js'; document.head.appendChild(script);"
    driver.execute_script(jquery_script)
    print(jquery_script)
    time.sleep(5)
    
    
    country = driver.execute_script("return $('#page-section-detail-seller-info div div div div:last-child')[0].innerText")
    print("country",country)
    if country == 'CN':
        print("Chinese Seller !!!")
        return None
    else:
        
        # seller_id
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        seller_id = query_params.get('seller')[0]
        print("seller_id",seller_id)
        
        # store_name
        store_name = driver.execute_script("return $('#seller-name')[0].innerText")
        print("store_name",store_name)
        
        # rating_num
        review_num = driver.execute_script("return $('#total-feedback-count-default')[0].innerText")
        print("review",int(review_num))
        
        ## detail information #################################################################
        detail_info = driver.execute_script("return $('#page-section-detail-seller-info')[0].innerText")
        notes2 = detail_info
        # print("notes2",detail_info)    
        
        # business_name
        business_name = re.search(r'Geschäftsname: (.+)', detail_info).group(1)
        print("business_name",business_name)
        
        # business_type
        business_type = re.search(r'Geschäftsart: (.+)', detail_info).group(1)
        print("business_type",business_type)
        
        # trade_register_number
        trade_register_num = re.search(r'Handelsregisternummer: (.+)', detail_info).group(1)
        print("trade_register_num",trade_register_num)
        
        # vat_number
        vat_id = re.search(r'UStID: (.+)', detail_info).group(1)
        print("vat_num:",vat_id)
        
        # match_number
        match = re.search(r'Geschäftsadresse:\n((?:.*\n)+)', detail_info)
        if match:
            business_address = match.group(1).replace('\n',' ')
            print("business_address:", business_address)
        
        # email
        match = re.search(r'E-Mail: (.+)', detail_info)
        if match:
            email=match.group(1)
        else:
            email=''       
        print("email:", email)
        # phone_number
        match = re.search(r'Telefonnummer: (.+)', detail_info)
        if match:
            phone_number = match.group(1)
        else:
            phone_number=''
        print("phone_number:", phone_number)
        
        # customer_service_address
        match = re.search(r'Kundendienstadresse:\n((?:.*\n)+)(?=Geschäftsadresse:)', detail_info)
        if match:
            # customer_service_address = match.group(1).strip()
            customer_service_address = match.group(1).replace('\n', ' ')
        else:
            customer_service_address=''   
        print("customer_service_address:", customer_service_address)
        
        
        ## about seller information #################################################################
        view_more_btn = None
        try:
            view_more_btn = driver.find_element(By.CSS_SELECTOR, "#spp-expander-about-seller div:last-of-type span a")
        except Exception as e:
            print("no view more>>>")
            pass
        if view_more_btn:
            jquery_code = "$('#spp-expander-about-seller div:last-of-type span a')[0].click()" 
            driver.execute_script(jquery_code)
            print("view more>>>>>>>>")
            time.sleep(5)    
        
        about_info = driver.execute_script("return $('#spp-expander-about-seller div')[0].innerText")
        notes1 = about_info
        # print("notes1:", about_info)
        
        # business_owner     
        match1 = re.search(r'Geschäftsführer: (.+)', about_info)
        match2 = re.search(r'Geschäftsführer (.+)', about_info)
        match3 = re.search(r'Geschäftsführende Direktoren: (.+)', about_info)
        match4 = re.search(r'Inhaber: (.+)', about_info)
        match5 = re.search(r'Inhaber (.+)', about_info)
        if match1:
            business_owner = match1.group(1)
        elif match2:
            business_owner = match2.group(1)
        elif match3:
            business_owner = match3.group(1)
        elif match4:
            business_owner = match4.group(1)
        elif match5:
            business_owner = match5.group(1)
        else:
            business_owner = ''       
        print("business_owner:", business_owner)
        # email_2
        match = re.search(r'E-Mail: (.+)', about_info)
        if match:
            email_2=match.group(1)
        else:
            email_2=''       
        print("email_2:", email_2)
        # telephone_2
        match = re.search(r'Telefon: (.+)', about_info)
        if match:
            phone_number_2 = match.group(1)
        else:
            phone_number_2=''
        print("telephone_2:", phone_number_2)
            
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
        
        data = {
            # 'link_id': seller_id,
            'store_name': store_name,
            'review': int(review_num),
            'detailed_link': url,
            'business_name': business_name,
            'business_owner': business_owner,
            'business_type': business_type,
            'amtsgericht': amtsgericht,
            'trade_register_number': trade_register_num,
            'vat_id': vat_id,
            'phone_number': phone_number,
            'phone_number_2': phone_number_2,
            'email': email,
            'email_2': email_2,
            'customer_service_address': customer_service_address,
            'business_address': business_address,
            'country':country,
            'notes1': notes1,
            'notes2': notes2,
        }
        
        return data
        # mydb.insert_sellerinfo(data)
    
    
    
    
