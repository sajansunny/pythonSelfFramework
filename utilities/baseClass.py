import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        option = (By.LINK_TEXT, text)
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located(option))
        self.driver.find_element(*option).click()

    def selectDropdown(self, locator, visible_text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(visible_text)
