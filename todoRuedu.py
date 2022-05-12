from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

print("Ingrese el correo a utilizar: ")
username = input()
print("Ingrese la contraseña a utilizar (debe tener mínimo 8 caracteres): ")
password = input()
print("Ingrese la contraseña a utilizar, para el cambio de contraseña (debe tener mínimo 8 caracteres): ")
newPassword = input()


############################# REGISTRO ###############################################

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

driver.find_element_by_id("pass").send_keys(password)

time.sleep(1)

driver.find_element_by_id("pass-confirm").send_keys(password)

time.sleep(1)

driver.find_element_by_id("button_form_inscription").click()

time.sleep(6)

driver.close()

time.sleep(2)

############################# INICIO DE SESION ###############################################

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

driver.find_element_by_id("login_pass").send_keys(password)

time.sleep(1)

driver.find_element_by_id("see-password").click()

time.sleep(3)

check_box = driver.find_element_by_xpath('//*[@id="form_login"]/div/button')
check_box.click()

time.sleep(6)

driver.close()

time.sleep(2)

############################# CAMBIO DE CONTRASEÑA ###############################################

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

driver.find_element_by_id("login_pass").send_keys(password)

time.sleep(1)

driver.find_element_by_id("see-password").click()

time.sleep(3)

check_box = driver.find_element_by_xpath('//*[@id="form_login"]/div/button')
check_box.click()

link = driver.find_element_by_link_text('Modifier mon mot de passe')
link.click()

time.sleep(1)

driver.find_element_by_id("pass-old").send_keys(password)

time.sleep(1)

driver.find_element_by_id("pass").send_keys(newPassword)

time.sleep(1)

driver.find_element_by_id("pass-confirm").send_keys(newPassword)

time.sleep(1)
check_box = driver.find_element_by_xpath('//*[@id="account-edit-compte"]/button')
check_box.click()

time.sleep(6)

driver.close()

time.sleep(2)

############################# COMPROBACION DE INCICIO DE SESION CON CONTRASEÑA NUEVA ###############################################

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

driver.find_element_by_id("login_pass").send_keys(newPassword)

time.sleep(1)

driver.find_element_by_id("see-password").click()

time.sleep(3)

check_box = driver.find_element_by_xpath('//*[@id="form_login"]/div/button')
check_box.click()

time.sleep(6)

driver.close()

time.sleep(2)

############################# REESTABLECIMIENTO DE CONTRASEÑA ###############################################

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

time.sleep(6)

driver.close()

time.sleep(2)