from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

import constants
from locators import Locators

class TestRegistration:
    def test_registration_success(self, driver, random_email):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(constants.NAME)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(constants.PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON_FORM).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.ENTER_BUTTON)))
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(constants.PASSWORD)
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        input_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.NAME_PERSONAL_DATA)))
        input_value = input_value.get_attribute('value')
        assert input_value == constants.NAME

    def test_registration_incorrect_password_warning(self, driver, random_email):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.NAME_INPUT).send_keys(constants.NAME)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(random_email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(random.randint(0, 99999))
        driver.find_element(*Locators.REGISTRATION_BUTTON_FORM).click()
        warning = WebDriverWait(driver, 5 ).until(EC.presence_of_element_located((Locators.WARNING_INCORRECT_PASSWORD)))
        assert warning.text == 'Некорректный пароль'

