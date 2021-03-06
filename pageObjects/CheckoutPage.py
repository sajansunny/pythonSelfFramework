from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    checkoutButton = (By.XPATH, "//a[@class = 'nav-link btn btn-primary']")

    def getCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)
