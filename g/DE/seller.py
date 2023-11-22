import requests
from bs4 import BeautifulSoup
import time, random

def get_seller(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0'
    }
    
    for i in range(3):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, "html.parser")   
            #verify whether seller is chinese or not
            country = soup.select_one("#page-section-detail-seller-info div div div div:last-child").text
            print('country:',country)
            if country == 'CN':
                print("Chinese Seller !!!")
            else:                
                # seller-name
                snelement = soup.select_one("#seller-name")
                if snelement:
                    seller_name = snelement.get_text()
                print(seller_name)
                
                # rating and feedback summary
                rfelement = soup.select_one("#seller-info-feedback-summary")
                if rfelement:
                    rating_feedback = rfelement.get_text()
                print(rating_feedback)
                
                # about seller
                aselement = soup.select_one("#page-section-about-seller")
                if aselement:
                    about_seller = aselement.get_text()
                print(about_seller)
                
                # rating and feedback summary
                dselement = soup.select_one("#page-section-detail-seller-info")
                if dselement:
                    detail_seller = dselement.get_text()
                print(detail_seller)
            break
        else:
            print("Request failed with status code:", response.status_code)
            time.sleep(10)
            
        
    
   
                    
    # if response.status_code == 200:
    #     # Parse the HTML content using BeautifulSoup
    #     soup = BeautifulSoup(response.content, "html.parser")   

    #     #verify whether seller is chinese or not
    #     country = soup.select_one("#page-section-detail-seller-info div div div div:last-child").text
    #     print('country:',country,file='log.txt')
    #     if country == 'CN':
    #         print("Chinese Seller !!!")
    #     else:                
    #         # seller-name
    #         snelement = soup.select_one("#seller-name")
    #         if snelement:
    #             rating_feedback = snelement.get_text()
    #         print(rating_feedback)
            
    #         # rating and feedback summary
    #         rfelement = soup.select_one("#seller-info-feedback-summary")
    #         if rfelement:
    #             rating_feedback = rfelement.get_text()
    #         print(rating_feedback)
            
    #         # about seller
    #         aselement = soup.select_one("#page-section-about-seller")
    #         if aselement:
    #             rating_feedback = aselement.get_text()
    #         print(rating_feedback)
            
    #         # rating and feedback summary
    #         dselement = soup.select_one("#page-section-detail-seller-info")
    #         if dselement:
    #             rating_feedback = dselement.get_text()
    #         print(rating_feedback)
        
    # else:
    #     print("Request failed with status code:", response.status_code)