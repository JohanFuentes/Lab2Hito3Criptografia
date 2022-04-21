from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "https://www.reebok.cl/account-login"

username = "ejemplocorreo@gmail.com"

time.sleep(1)
driver = webdriver.Chrome()

url = "https://www.reebok.cl/account-login"

driver.get(url)

time.sleep(2)

link = driver.find_element_by_link_text('¿Has olvidado tu contraseña?')

link.click()

time.sleep(2)

driver.find_element_by_name("email").send_keys(username)

time.sleep(2)

check_box = driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/div/div[2]/form/div[4]/div/button')
check_box.click()

time.sleep(10)

driver.close()

time.sleep(2)
