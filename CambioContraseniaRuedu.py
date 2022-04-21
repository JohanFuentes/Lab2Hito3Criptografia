from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "https://www.rueducommerce.fr/login.html?crea=1"

username = "ejemplocorreo@gmail.com"
newPassword = "Password1234"

time.sleep(1)
driver = webdriver.Chrome()

url = "https://www.rueducommerce.fr/login.html?crea=1"

driver.get(url)

time.sleep(1)

driver.find_element_by_id("rgpd-btn-index-accept").click()

time.sleep(1)

driver.find_element_by_id("box-content-item-link-1").click()

time.sleep(1)

driver.find_element_by_id("login").send_keys(username)

time.sleep(1)

driver.find_element_by_id("login_pass").send_keys("Prueba1234.")

time.sleep(1)
check_box = driver.find_element_by_xpath('//*[@id="form_login"]/div/button')
check_box.click()

link = driver.find_element_by_link_text('Modifier mon mot de passe')
link.click()

time.sleep(1)

driver.find_element_by_id("pass-old").send_keys("Prueba1234.")

time.sleep(1)

driver.find_element_by_id("pass").send_keys(newPassword)

time.sleep(1)

driver.find_element_by_id("pass-confirm").send_keys(newPassword)

time.sleep(1)
check_box = driver.find_element_by_xpath('//*[@id="account-edit-compte"]/button')
check_box.click()

time.sleep(10)

driver.close()

time.sleep(2)
