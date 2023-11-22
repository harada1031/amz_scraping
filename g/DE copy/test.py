import re
import mydb

def extract_dp_value(url):
    pattern = r'dp/(\w+)/'
    pattern2 = r'dp%2F(\w+)%2F'
    match = re.search(pattern, url)
    match2 = re.search(pattern2, url)
    if match:
        return match.group(1)
    elif match2:
        return match2.group(1)
    else:
        return None

url1 = "https://www.amazon.de/Reflexhammer-nach-Tr%C3%B6mner-Black-Edition/dp/B017KRBX88/ref=pd_sbs_sccl_3_2/262-4336584-4094515?pd_rd_w=1pGUP&content-id=amzn1.sym.6c0521be-6c2b-450c-bb72-af8082730381&pf_rd_p=6c0521be-6c2b-450c-bb72-af8082730381&pf_rd_r=4J92FQQNBMHCDH7WH8P4&pd_rd_wg=5nvjO&pd_rd_r=03c8deaa-6208-4cfb-8014-ff1d0d3f72fc&pd_rd_i=B017KRBX88&psc=1"
url2 = "https://www.amazon.de/sspa/click?ie=UTF8&spc=MTozNDczMzQ3NjYxMzM2Njc0OjE2OTkyNDk0NjQ6c3BfZGV0YWlsOjIwMDc4NTY3OTY5NDAxOjo6Og&url=%2Fdp%2FB097TWY1YM%2Fref%3Dsspa_dk_detail_1%3Fpsc%3D1%26pd_rd_i%3DB097TWY1YM%26pd_rd_w%3D05QDs%26content-id%3Damzn1.sym.ae2317a0-2175-4285-af64-66539858231f%26pf_rd_p%3Dae2317a0-2175-4285-af64-66539858231f%26pf_rd_r%3D4J92FQQNBMHCDH7WH8P4%26pd_rd_wg%3D5nvjO%26pd_rd_r%3D03c8deaa-6208-4cfb-8014-ff1d0d3f72fc%26s%3Dindustrial%26sp_csd%3Dd2lkZ2V0…"

dp_value1 = extract_dp_value(url1)
dp_value2 = extract_dp_value(url2)

print("dp value from the first URL:", "%"+dp_value1+"%")
print("dp value from the second URL:", dp_value2)
