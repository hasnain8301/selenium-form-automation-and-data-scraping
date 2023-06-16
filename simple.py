from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('https://codeaza-apps.com/formvalidation.html')

# Input Name 
name_input = driver.find_element(By.ID, "name")
name_input.send_keys('Hasnain Nafees')

# Input Email 
email_input = driver.find_element(By.ID, "email")
email_input.send_keys('hasnain@gmail.com')

# Input password 
password_input = driver.find_element(By.ID, "password")
password_input.send_keys('password123')


# Input age 
age_input = driver.find_element(By.ID, "age")
age_input.send_keys(26)

# Input gender 
gender_input = driver.find_element(By.ID, "gender")
select_gender = Select(gender_input)
select_gender.select_by_value('male')

# Input date 
date_input = driver.find_element(By.ID, "birthdate")
date_input.send_keys('06/30/1997')


# Input address 
address_input = driver.find_element(By.ID, "address")
address_input.send_keys('Block 12 chowk. Sargodha, Pakistan')

# Input image 
image_input = driver.find_element(By.ID, "image")
image_input.send_keys('E:\OFFICE\Selenium\profile.jpg')


# Input color 
color_input = driver.find_element(By.ID, "color")
color_input.send_keys('#FF0000')

# Input url 
url_input = driver.find_element(By.ID, "website")
url_input.send_keys('https://hasnainnafees.com/')


# Input checkbox 
checkbox_input = driver.find_element(By.ID, "subscribe")
if not checkbox_input.is_selected():
    checkbox_input.click()


# Input interest1 
interest1_input = driver.find_element(By.ID, "interest1")
if not interest1_input.is_selected():
    interest1_input.click()

# Input interest2
interest2_input = driver.find_element(By.ID, "interest2")
if not interest2_input.is_selected():
    interest2_input.click()

# Input interest3
interest3_input = driver.find_element(By.ID, "interest3")
if not interest3_input.is_selected():
    interest3_input.click()

submit_input = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()



sleep(10)
driver.quit()