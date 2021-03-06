import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from pageObjects.ShopPage import ShopPage
from utilities.baseClass import BaseClass


class TestOne(BaseClass):

    def test_endToEnd(self):
        home_page = HomePage(self.driver)
        home_page.shop_link().click()
        shop_page = ShopPage(self.driver)
        product_names = shop_page.getCardTitles()
        checkout_page = CheckoutPage(self.driver)
        checkout_button = checkout_page.getCheckoutButton()
        i = -1
        for product_name in product_names:
            i = i+1
            if product_name.text == "Blackberry":
                shop_page.getFooterButtons()[i].click()
                break
        checkout_button.click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_xpath("//input[@id='country']").send_keys("Ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        checkbox = self.driver.find_element_by_xpath("//input[@id='checkbox2']")
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.driver.find_element_by_xpath("//input[@type='submit']").click()
        assert "Thank you" in self.driver.find_element_by_class_name("alert-success").text
        self.driver.get_screenshot_as_file("endToEnd.png")
