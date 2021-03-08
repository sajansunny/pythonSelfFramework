from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countryTextbox = (By.XPATH, "//input[@id='country']")
    confirmCheckbox = (By.XPATH, "//input[@id='checkbox2']")
    purchaseButton = (By.XPATH, "//input[@type='submit']")
    successAlert = (By.CLASS_NAME, "alert-success")

    def getCountryTextbox(self):
        return self.driver.find_element(*ConfirmPage.countryTextbox)

    def getConfirmCheckbox(self):
        return self.driver.find_element(*ConfirmPage.confirmCheckbox)

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def getSuccessAlert(self):
        return self.driver.find_element(*ConfirmPage.successAlert)
