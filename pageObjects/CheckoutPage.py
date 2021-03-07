from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    confirmCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']")

    def getConfirmCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.confirmCheckoutButton)
