from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

print("Ingrese el correo a utilizar: ")
username = input()
print("Ingrese la contraseña a utilizar (debe tener mínimo 8 caracteres, una mayúscula, una minúscula y un número): ")
password = input()
print("Ingrese la contraseña a utilizar, para el cambio de contraseña (debe tener mínimo 8 caracteres, una mayúscula, una minúscula y un número): ")
newPassword = input()


############################# REGISTRO ###############################################

driver = webdriver.Chrome()

url = "https://www.reebok.cl/account-register"

driver.get(url)

time.sleep(3)

driver.find_element_by_name("firstName").send_keys("juan")

time.sleep(1)

driver.find_element_by_name("lastName").send_keys("valdes")

time.sleep(1)

driver.find_element_by_name("day").send_keys("12")

time.sleep(1)

driver.find_element_by_name("month").send_keys("11")

time.sleep(1)

driver.find_element_by_name("year").send_keys("1997")

time.sleep(1)

check_box1 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/div[4]/section/div/div/label[1]/input')
actions1 = webdriver.ActionChains(driver)
actions1.move_to_element_with_offset(check_box1, 0, 0).perform()
actions1.click().perform()

driver.find_element_by_name("email").send_keys(username)

time.sleep(1)

driver.find_element_by_name("password").send_keys(password)

time.sleep(1)

check_box2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/div[9]/div/div/label/input')
actions2 = webdriver.ActionChains(driver)
actions2.move_to_element_with_offset(check_box2, 24, 24).perform()
actions2.click().perform()

time.sleep(1)

check_box3 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/button')
check_box3.click()

time.sleep(6)

driver.close()

time.sleep(2)

############################# INICIO DE SESION ###############################################

driver = webdriver.Chrome()

url = "https://www.reebok.cl/account-login"

driver.get(url)

time.sleep(3)

driver.find_element_by_id("login-email").send_keys(username)

time.sleep(1)

driver.find_element_by_id("login-password").send_keys(password)

time.sleep(1)

s = driver.find_element_by_css_selector("button[class='gl-cta gl-cta--tertiary show-hide-password-button___2RTy0']")
s.click()

time.sleep(3)

check_box = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/div[7]/button')
check_box.click()

time.sleep(10)

driver.close()

time.sleep(2)

############################# CAMBIO DE CONTRASEÑA ###############################################

driver = webdriver.Chrome()

url = "https://www.reebok.cl/account-login"

driver.get(url)

time.sleep(3)

driver.find_element_by_id("login-email").send_keys(username)

time.sleep(1)

driver.find_element_by_id("login-password").send_keys(password)

time.sleep(1)
s = driver.find_element_by_css_selector("button[class='gl-cta gl-cta--tertiary show-hide-password-button___2RTy0']")
s.click()
time.sleep(3)

check_box = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/div[7]/button')
check_box.click()

time.sleep(8)

link = driver.find_element_by_link_text('Datos personales')

link.click()

time.sleep(8)

s = driver.find_element_by_css_selector("button[data-auto-id='edit-profile-information-button-PASSWORD_MODAL']")
s.click()

time.sleep(1)

driver.find_element_by_name("oldPassword").send_keys(password)

time.sleep(2)

driver.find_element_by_name("newPassword").send_keys(newPassword)

s1 = driver.find_element_by_css_selector("button[data-auto-id='personal-info:button.submit']")
s1.click()

time.sleep(6)

driver.close()

time.sleep(2)

############################# COMPROBACION DE INCICIO DE SESION CON CONTRASEÑA NUEVA ###############################################

driver = webdriver.Chrome()

url = "https://www.reebok.cl/account-login"

driver.get(url)

time.sleep(3)

driver.find_element_by_id("login-email").send_keys(username)

time.sleep(1)

driver.find_element_by_id("login-password").send_keys(newPassword)

time.sleep(1)
s = driver.find_element_by_css_selector("button[class='gl-cta gl-cta--tertiary show-hide-password-button___2RTy0']")
s.click()
time.sleep(3)

check_box = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/div[7]/button')
check_box.click()

time.sleep(10)

driver.close()

time.sleep(2)

############################# REESTABLECIMIENTO DE CONTRASEÑA ###############################################

driver = webdriver.Chrome()

url = "https://www.reebok.cl/account-login"

driver.get(url)

time.sleep(3)

link = driver.find_element_by_link_text('¿Has olvidado tu contraseña?')

link.click()

time.sleep(2)

driver.find_element_by_name("email").send_keys(username)

time.sleep(2)

check_box = driver.find_element_by_xpath('//*[@id="modal-root"]/div/div/div/div[2]/form/div[4]/div/button')
check_box.click()

time.sleep(6)

driver.close()

time.sleep(2)
