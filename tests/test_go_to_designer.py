from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestGoToDesigner:
    def test_go_to_designer_from_account_with_designer_button(self, driver, login):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.LOGIN_PERSONAL_DATA))
        driver.find_element(*Locators.DESIGNER).click()
        WebDriverWait(driver,5).until(EC.presence_of_element_located(Locators.ASSEMBLE_BURGER))
        buns = driver.find_element(*Locators.BUNS)
        assert buns.is_displayed()

    def test_go_to_designer_from_account_with_logo_click(self, driver, login):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.LOGIN_PERSONAL_DATA))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver,5).until(EC.presence_of_element_located(Locators.ASSEMBLE_BURGER))
        buns = driver.find_element(*Locators.BUNS)
        assert buns.is_displayed()


