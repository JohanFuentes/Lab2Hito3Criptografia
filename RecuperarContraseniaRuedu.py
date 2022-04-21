from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "https://www.rueducommerce.fr/password/email"

username = "ejemplocorreo@gmail.com"

time.sleep(1)
driver = webdriver.Chrome()

url = "https://www.rueducommerce.fr/password/email"

driver.get(url)

time.sleep(3)

driver.find_element_by_id("rgpd-btn-index-accept").click()

time.sleep(1)

driver.find_element_by_id("email").send_keys(username)

time.sleep(1)
check_box = driver.find_element_by_xpath('//*[@id="auth-password"]/form/div[2]/button')
check_box.click()

time.sleep(8)

driver.close()

time.sleep(2)