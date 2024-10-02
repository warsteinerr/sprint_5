from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC

class TestDesigner:
    def test_select_sauces_in_designer(self, driver, login):
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(Locators.SAUCES))
        driver.find_element(*Locators.SAUCES).click()
        chosen_element = driver.find_element(*Locators.SELECTED_PART).text
        assert chosen_element == 'Соусы'

    def test_select_buns_in_designer(self, driver, login):
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(Locators.SAUCES))
        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.BUNS).click()
        chosen_element = driver.find_element(*Locators.SELECTED_PART).text
        assert chosen_element == 'Булки'

    def test_select_fillings_in_designer(self, driver, login):
        WebDriverWait(driver, 4).until(EC.presence_of_element_located(Locators.SAUCES))
        driver.find_element(*Locators.FILLINGS).click()
        chosen_element = driver.find_element(*Locators.SELECTED_PART).text
        assert chosen_element == 'Начинки'
