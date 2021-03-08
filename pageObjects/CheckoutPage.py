from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    confirmCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")

    def getConfirmCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.confirmCheckoutButton).click()
        confirm_purchase_page = ConfirmPage(self.driver)
        return confirm_purchase_page
