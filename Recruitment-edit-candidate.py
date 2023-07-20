#edit data candidate

import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

import constant
import utils

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window() 
    driver.implicitly_wait(10)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield driver

def test_edit(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.NAME, 'username').send_keys("Admin")
    driver.find_element(
        By.NAME, 'password').send_keys("admin123"+ Keys.ENTER)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/recruitment/viewRecruitmentModule"]').click()
    
    driver.find_element(
        By.XPATH, '//i[@class="oxd-icon bi-eye-fill"]').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '//i[@class="oxd-icon bi-pencil-fill"]').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '//textarea[@placeholder="Type here"]').send_keys("Gagal")
    sleep(2)
    driver.find_element(
        By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
    sleep(2)