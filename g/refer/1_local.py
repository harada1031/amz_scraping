from asyncio.windows_events import CONNECT_PIPE_INIT_DELAY
# from asyncio import CONNECT_PIPE_INIT_DELAY
from os import link
from re import X
from selenium import webdriver
import time


chrome_profile_directory = "C:\\Users\\777\\AppData\\Local\\Google\\Chrome\\User Data\\Profile7"
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_directory}")
driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
time.sleep(100)