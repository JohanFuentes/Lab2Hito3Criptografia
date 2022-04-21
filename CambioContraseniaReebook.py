from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "https://www.reebok.cl/account-login"

username = "ejemplocorreo@gmail.com"
newPassword = "Password1234"

time.sleep(1)
driver = webdriver.Chrome()

url = "https://www.reebok.cl/account-login"

driver.get(url)

time.sleep(1)

driver.find_element_by_id("login-email").send_keys(username)

time.sleep(1)

driver.find_element_by_id("login-password").send_keys("Prueba1234.")

time.sleep(3)

check_box = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/div[7]/button')
check_box.click()

time.sleep(12)

link = driver.find_element_by_link_text('Datos personales')

link.click()

time.sleep(10)

s = driver.find_element_by_css_selector("button[data-auto-id='edit-profile-information-button-PASSWORD_MODAL']")
s.click()

time.sleep(1)

driver.find_element_by_name("oldPassword").send_keys("Prueba1234.")

time.sleep(2)

driver.find_element_by_name("newPassword").send_keys(newPassword)

s1 = driver.find_element_by_css_selector("button[data-auto-id='personal-info:button.submit']")
s1.click()

time.sleep(12)

driver.close()

time.sleep(5)