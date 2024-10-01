import pytest
from selenium import webdriver
import random
import string
from locators import Locators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()

@pytest.fixture
def random_email(domain="example.com"):
    random_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
    return f"{random_username}@{domain}"


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_INPUT).send_keys('semenkulagin14666@gmail.com')
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
    driver.find_element(*Locators.ENTER_BUTTON).click()
