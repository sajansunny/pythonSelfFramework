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
        log = self.getLogger()
        home_page = HomePage(self.driver)
        shop_page = home_page.shop_link()
        product_names = shop_page.getCardTitles()
        log.info("Getting product names..")

        i = -1
        for product_name in product_names:
            i = i+1
            if product_name.text == "Blackberry":
                shop_page.getFooterButtons()[i].click()
                log.info("Product 'Blackberry' selected")
                break

        confirm_checkout_page = shop_page.getCheckoutButton()
        confirm_purchase_page = confirm_checkout_page.getConfirmCheckoutButton()
        confirm_purchase_page.getCountryTextbox().send_keys("Ind")
        log.info("Entered the text as 'Ind'")
        self.verifyLinkPresence("India")
        confirm_checkbox = confirm_purchase_page.getConfirmCheckbox()
        self.driver.execute_script("arguments[0].click();", confirm_checkbox)
        confirm_purchase_page.getPurchaseButton().click()
        log.info("User confirmed the purchase")
        assert "Thank you" in confirm_purchase_page.getSuccessAlert().text
        log.info("Successfully purchased")
        self.driver.get_screenshot_as_file("endToEnd.png")
