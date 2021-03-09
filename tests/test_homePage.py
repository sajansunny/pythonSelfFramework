from selenium.webdriver.support.select import Select
import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.baseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        log.info("Name is " + getData["name"])
        home_page.getNameTextbox().send_keys(getData["name"])
        home_page.getEmailTextbox().send_keys(getData["email"])
        home_page.getIcecreamLoverCheckbox().click()
        self.selectDropdown(home_page.getGenderDropdown(), getData["gender"])
        home_page.getSubmitButton().click()
        alert_text = home_page.getAlertText()
        log.info(alert_text)
        assert "success" in alert_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
