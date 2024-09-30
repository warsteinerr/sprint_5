from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def test_login_main_page_positive(self, driver):
        driver.find_element(*Locators.MAIN_PAGE_LOGIN).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('semenkulagin14666@gmail.com')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        input_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.LOGIN_PERSONAL_DATA)))
        input_value = input_value.get_attribute('value')
        assert input_value == 'semenkulagin14666@gmail.com'

    def test_login_through_personal_account_button_positive(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('semenkulagin14666@gmail.com')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        input_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.LOGIN_PERSONAL_DATA)))
        input_value = input_value.get_attribute('value')
        assert input_value == 'semenkulagin14666@gmail.com'

    def test_login_through_enter_button_in_registration_form_positive(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        driver.find_element(*Locators.ENTER_IN_REGISTRATION).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('semenkulagin14666@gmail.com')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        input_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.LOGIN_PERSONAL_DATA)))
        input_value = input_value.get_attribute('value')
        assert input_value == 'semenkulagin14666@gmail.com'

    def test_login_through_recover_password_positive(self,driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.RECOVER_PASSWORD).click()
        driver.find_element(*Locators.ENTER_IN_REGISTRATION).click()
        driver.find_element(*Locators.EMAIL_INPUT).send_keys('semenkulagin14666@gmail.com')
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys('123456')
        driver.find_element(*Locators.ENTER_BUTTON).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        input_value = WebDriverWait(driver, 10).until(EC.presence_of_element_located((Locators.LOGIN_PERSONAL_DATA)))
        input_value = input_value.get_attribute('value')
        assert input_value == 'semenkulagin14666@gmail.com'




