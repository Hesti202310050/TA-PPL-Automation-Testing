#menghapus data pada menu admin qualifications education

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
    

def test_delete(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.NAME, 'username').send_keys("Admin")
    driver.find_element(
        By.NAME, 'password').send_keys("admin123"+ Keys.ENTER)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]').click()
    driver.find_element(
        By.XPATH, '//span[contains(text(),"Qualifications")]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//li//a[contains(text(),"Education")]').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '//i[@class="oxd-icon bi-trash"]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]').click()
    sleep(2)
def test_cancel(driver):
    characters = string.ascii_letters + string.digits + string.punctuation
    randomString = ''.join(random.choice(characters) for i in range(8))
    driver.find_element(
        By.NAME, 'username').send_keys("Admin")
    driver.find_element(
        By.NAME, 'password').send_keys("admin123"+ Keys.ENTER)
    driver.find_element(
        By.XPATH, '//a[@href="/web/index.php/admin/viewAdminModule"]').click()
    driver.find_element(
        By.XPATH, '//span[contains(text(),"Qualifications")]').click()
    sleep(1)
    driver.find_element(
        By.XPATH, '//li//a[contains(text(),"Education")]').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '//i[@class="oxd-icon bi-trash"]').click()
    sleep(2)
    driver.find_element(
        By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--text orangehrm-button-margin"]').click()
    sleep(1)