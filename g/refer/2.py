import time
import requests


# url = 'https://www.amazon.de/sp?ie=UTF8&seller=A1K6TAQBRYGCP&asin=B097TTLDSP&ref_=dp_merchant_link&isAmazonFulfilled=1'
url = 'https://www.amazon.de/tee-uu-PULL-Handschuh-Holster-10-5cm/dp/B06WVD8C6H/ref=pd_rhf_d_dp_s_pd_crcd_sccl_2_5/261-4023725-9615548?pd_rd_w=DjG3d&content-id=amzn1.sym.d36cdb68-efc9-4a4e-bcda-d349636a649b&pf_rd_p=d36cdb68-efc9-4a4e-bcda-d349636a649b&pf_rd_r=W40A5R74BVG1T3863J7P&pd_rd_wg=epHVA&pd_rd_r=5ddf1335-44d5-49de-9b5a-8dde24afaa5c&pd_rd_i=B06WVD8C6H&psc=1'
headers = {
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:93.0) Gecko/20100101 Firefox/93.0'
}
response = requests.get(url, headers=headers)
time.sleep(10)
print(response.content,response.status_code)
print("-----------")
time.sleep(1000)
