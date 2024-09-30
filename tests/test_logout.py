from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestLogout:
    def test_logout_with_logout_button(self, driver, login):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.LOGOUT))
        driver.find_element(*Locators.LOGOUT).click()
        WebDriverWait(driver,5).until(EC.presence_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
