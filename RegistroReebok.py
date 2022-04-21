from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "https://www.reebok.cl/account-register"

username = "ejemplocorreo@gmail.com"

time.sleep(1)
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

driver.find_element_by_name("password").send_keys("Prueba1234.")

time.sleep(1)

check_box2 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/div[9]/div/div/label/input')
actions2 = webdriver.ActionChains(driver)
actions2.move_to_element_with_offset(check_box2, 24, 24).perform()
actions2.click().perform()

time.sleep(1)

check_box3 = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/button')
check_box3.click()

time.sleep(20)

driver.close()

time.sleep(2)
