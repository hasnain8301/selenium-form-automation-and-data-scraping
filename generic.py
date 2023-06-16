from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import random


driver = webdriver.Chrome()
driver.get('https://codeaza-apps.com/formvalidation.html')


# Define locators for form elements
name_input = (By.ID, "name")
email_input = (By.ID, "email")
password_input = (By.ID, "password")
age_input = (By.ID, "age")
gender_input = (By.ID, "gender")
date_input = (By.ID, "birthdate")
address_input = (By.ID, "address")
image_input = (By.ID, "image")
color_input = (By.ID, "color")
url_input = (By.ID, "website")
checkbox_input = (By.ID, "subscribe")
interest1_input = (By.ID, "interest1")
interest2_input = (By.ID, "interest2")
interest3_input = (By.ID, "interest3")

form_data = {
    "name" : 'Hasnain Nafees', 
    "email" : 'hasnain@gmail.com',
    "password" : 'password123', 
    "age" : 26,
    "gender" : 'male', 
    "birthdate" : '06/30/1997', 
    "address" : 'Block 12 chowk. Sargodha, Pakistan', 
    "image" : 'E:\OFFICE\Selenium\profile.jpg', 
    "color" : '#FF0000', 
    "website" : 'https://hasnainnafees.com/', 
    "subscribe" : True,
    "interest1" :False, 
    "interest2" :True,
    "interest3" :True
}

def enter_age_check(locator, value):
    element = driver.find_element(*locator)
    min_age = element.get_attribute('min')
    max_age = element.get_attribute('max')
    age = random.randint(int(min_age), int(max_age))
    time.sleep(2)
    element.send_keys(age)

def enter_text_slowly(element, text, delay=0.1):
    for char in text:
        element.send_keys(char)
        time.sleep(delay)

def input_text(locator, value):
    element = driver.find_element(*locator)
    element.clear()
    enter_text_slowly(element, value)

def input_simple(locator, value):
    element = driver.find_element(*locator)
    element.clear()
    time.sleep(2)
    element.send_keys(value)
    

def set_checkbox(locator, value):
    checkbox_element = driver.find_element(*locator)
    if value and not checkbox_element.is_selected():
        time.sleep(1)
        checkbox_element.click()
    elif not value and checkbox_element.is_selected():
        time.sleep(1)
        checkbox_element.click()

def select_option(locator, value):
    select_element = Select(driver.find_element(*locator))
    time.sleep(1)
    select_element.select_by_value(value)




for field, value in form_data.items():
    if field == "name":
        input_text(name_input, value)
    elif field == "email":
        input_text(email_input, value)
    elif field == "password":
        input_text(password_input, value)
    elif field == "age":
        enter_age_check(age_input, value)
    elif field == "gender":
        select_option(gender_input, value)
    elif field == "birthdate":
        input_simple(date_input, value)
    elif field == "address":
        input_text(address_input, value)
    elif field == "image":
        input_simple(image_input, value)
    elif field == "color":
        input_simple(color_input, value)
    elif field == "website":
        input_text(url_input, value)
    elif field == "subscribe":
        set_checkbox(checkbox_input, value)
    elif field == "interest1":
        set_checkbox(interest1_input, value)
    elif field == "interest2":
        set_checkbox(interest2_input, value)
    elif field == "interest3":
        set_checkbox(interest3_input, value)

submit_input = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

time.sleep(10)
driver.quit()