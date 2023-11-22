how can I get the state when page down button is longer available. I mean when scroll is at the end
=
To detect when the scroll reaches the end of a page during web scraping using Python, you can utilize a headless browser like Selenium. Here's an example using Selenium and Chrome WebDriver:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get('https://example.com')

# Wait for the page to load completely
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Scroll to the end of the page
while True:
    # Get the current scroll height
    prev_height = driver.execute_script('return document.body.scrollHeight')
    
    # Scroll to the bottom of the page
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
    # Wait for the page to load new content (if any)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    
    # Get the new scroll height after scrolling
    new_height = driver.execute_script('return document.body.scrollHeight')
    
    # Check if the scroll height remains the same, indicating that we've reached the end of the page
    if new_height == prev_height:
        break

# Perform any actions you need when the scroll is at the end
# For example, you can scrape data from the fully loaded page

# Close the browser
driver.quit()
```

In this example, we use Selenium to open a webpage and scroll to the end of the page. The `while` loop continuously scrolls down until the scroll height no longer increases, indicating that we've reached the end of the page. You can then perform any scraping actions or data extraction from the fully loaded page.

Make sure you have Selenium and Chrome WebDriver installed. You can install them using pip:

```
pip install selenium
```

Also, ensure that you have the appropriate Chrome WebDriver executable file for your operating system and Chrome version. You can download it from the official Selenium website (https://www.selenium.dev/documentation/en/webdriver/driver_requirements/).