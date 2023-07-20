from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import constant

def login(driver):
    driver.find_element(
        By.ID, 'username').send_keys(constant.USERNAME)
    driver.find_element(
        By.ID, 'password').send_keys(constant.PASSWORD + Keys.ENTER)

