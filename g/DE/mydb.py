import pymysql
import re

# Basic --------------------------------------------------------------------------------
def db_connect(host, port, username, password, dbname):
    db = pymysql.connect(host=host, port=port, user=username, password=password, database=dbname)
    return db
def db_close(db):
    db.close()

# Links table --------------------------------------------------------------------------------
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
        return url

def is_already_added(db, link):
    cursor= db.cursor()
    sql = "select * from links where link like %s"
    dp = extract_dp_value(link)
    value = "%"+dp+"%"
    cursor.execute(sql, value) 
    num = cursor.rowcount
    db.commit()
    cursor.close()
    return int(num)
    
def insert_link(db,link):
    cursor= db.cursor()
    sql = "INSERT INTO links (link, is_used) VALUES (%s, %s)"
    values = (link, 0)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()

def update_link(db, link):
    cursor = db.cursor()
    update_query = "UPDATE links SET is_used = %s WHERE link = %s"
    update_values = (1, link)
    cursor.execute(update_query, update_values)
    db.commit()
    cursor.close()
    
def next_link(db):
    cursor= db.cursor()
    sql = "select link from links where is_used = 0 LIMIT 1"
    cursor.execute(sql)
    n_url = cursor.fetchone()[0]
    db.commit()
    cursor.close()
    return str(n_url)


# Sellers table --------------------------------------------------------------------------------
def is_sellerinfo_exist(db, link):
    cursor= db.cursor()
    sql = "select * from detailed_seller_info where seller_page_link = %s"
    values = (link)
    cursor.execute(sql, values) 
    num = cursor.rowcount
    db.commit()
    cursor.close()
    return int(num)


def is_sellerid_exist(db, seller_id):
    cursor= db.cursor()
    sql = "select * from detailed_seller_info where detailed_link like %s"
    values = "%"+seller_id+"%"
    cursor.execute(sql, values) 
    num = cursor.rowcount
    db.commit()
    cursor.close()
    return int(num)

def insert_sellerinfo(db, data):
    cursor= db.cursor()
    sql = "INSERT INTO detailed_seller_info (store_name, detailed_link, business_name, business_owner, review, business_type, amtsgericht, trade_register_number, vat_id, business_address, phone_number, email, customer_service_address, email_2, phone_number_2, country, notes1, notes2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (data['store_name'],data['detailed_link'],data['business_name'],data['business_owner'],data['review'],data['business_type'],data['amtsgericht'],data['trade_register_number'],data['vat_id'],data['business_address'],data['phone_number'],data['email'],data['customer_service_address'],data['email_2'],data['phone_number_2'],data['country'],data['notes1'],data['notes2'])
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
