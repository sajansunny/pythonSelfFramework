import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from utilities.baseClass import BaseClass


class TestOne(BaseClass):

    def test_endToEnd(self):
        home_page = HomePage(self.driver)
        home_page.shop_link().click()
        shop_page = ShopPage(self.driver)
        product_names = shop_page.getCardTitles()
        # checkout_page = CheckoutPage(self.driver)
        checkout_button = shop_page.getCheckoutButton()
        i = -1
        for product_name in product_names:
            i = i+1
            if product_name.text == "Blackberry":
                shop_page.getFooterButtons()[i].click()
                break
        checkout_button.click()

        confirm_checkout_page = CheckoutPage(self.driver)
        confirm_checkout_page.getConfirmCheckoutButton().click()

        confirm_purchase_page = ConfirmPage(self.driver)
        confirm_purchase_page.getCountryTextbox().send_keys("Ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located(ConfirmPage.indiaOption))
        confirm_purchase_page.getIndiaOption().click()
        confirm_checkbox = confirm_purchase_page.getConfirmCheckbox()
        self.driver.execute_script("arguments[0].click();", confirm_checkbox)
        confirm_purchase_page.getPurchaseButton().click()
        assert "Thank you" in confirm_purchase_page.getSuccessAlert().text
        self.driver.get_screenshot_as_file("endToEnd.png")
