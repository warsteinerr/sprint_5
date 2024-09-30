from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestPersonalPage:
    def test_go_to_personal_page_unlogged(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver,5).until(EC.presence_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    def test_go_to_personal_page_logged(self, driver, login):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.LOGIN_PERSONAL_DATA))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

