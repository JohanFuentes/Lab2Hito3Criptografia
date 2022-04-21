from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "https://www.rueducommerce.fr/login.html?crea=1"

username = "ejemplocorreo@gmail.com"

time.sleep(1)
driver = webdriver.Chrome()

url = "https://www.rueducommerce.fr/login.html?crea=1"

driver.get(url)

time.sleep(3)

driver.find_element_by_id("rgpd-btn-index-accept").click()

time.sleep(1)

driver.find_element_by_name("email").send_keys(username)

time.sleep(1)

driver.find_element_by_id("creation_compte_toggle").click()

time.sleep(1)

check_box1 = driver.find_element_by_xpath('//*[@id="civilite_M"]')
print(check_box1.size)
actions1 = webdriver.ActionChains(driver)
actions1.move_to_element_with_offset(check_box1, 0, 0).perform()
actions1.click().perform()

time.sleep(1)

driver.find_element_by_name("prenom").send_keys("juan")

time.sleep(1)

driver.find_element_by_name("nom").send_keys("valdes")

time.sleep(1)

driver.find_element_by_name("jour").send_keys("12")

time.sleep(1)

driver.find_element_by_name("mois").send_keys("10")

time.sleep(1)

driver.find_element_by_name("annee").send_keys("1995")

time.sleep(1)

driver.find_element_by_id("pass").send_keys("Prueba1234.")

time.sleep(1)

driver.find_element_by_id("pass-confirm").send_keys("Prueba1234.")

time.sleep(1)

driver.find_element_by_id("button_form_inscription").click()

time.sleep(10)

driver.close()

time.sleep(2)