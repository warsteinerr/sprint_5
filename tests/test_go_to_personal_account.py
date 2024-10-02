from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
import constants

class TestPersonalPage:
    def test_go_to_personal_page_unlogged(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver,5).until(EC.presence_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == constants.LOGIN_PAGE_LINK

    def test_go_to_personal_page_logged(self, driver, login):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.LOGIN_PERSONAL_DATA))
        assert driver.current_url == constants.ACCOUNT_PAGE_LINK

