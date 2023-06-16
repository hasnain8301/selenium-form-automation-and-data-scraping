from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os
from save_data import Add_data_to_File



driver = webdriver.Chrome()
driver.get('https://quotes.toscrape.com/login')
# Fill Username field
username = driver.find_element(By.ID, "username")
username.send_keys('admin')
# Fill Password field
password = driver.find_element(By.ID, "password")
password.send_keys('admin')
# Click Submit Button
driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

wait = WebDriverWait(driver, 10)
next_page_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//p/a[text()='Logout']")))

def handle_pagination(end_page):
    for i in range(end_page):
        # Wait for the next page to load
        
        all_quotes_on_page = driver.find_elements(By.CLASS_NAME, "quote")
        for quote in all_quotes_on_page:
            data_list = []
            quote_text = quote.find_element(By.CLASS_NAME, "text")
            quote_author = quote.find_element(By.CLASS_NAME, "author")
            quote_tags = quote.find_elements(By.CLASS_NAME, "tag")
            tags = []
            for tag in quote_tags:
                tags.append(tag.text)

            data_list.append(quote_text.text)
            data_list.append(quote_author.text)
            data_list.append(tags)
            Add_data_to_File(data_list)
        time.sleep(2)
        driver.find_element(By.XPATH, "//li[contains(@class, 'next')]/a[text()='Next ']").click()


handle_pagination(5)
    
time.sleep(10)
driver.quit()


