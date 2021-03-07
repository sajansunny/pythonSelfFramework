from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitles = (By.XPATH, "//h4[@class='card-title']")
    footerButtons = (By.CSS_SELECTOR, ".card-footer button")
    checkoutButton = (By.XPATH, "//a[@class = 'nav-link btn btn-primary']")


    def getCardTitles(self):
        return self.driver.find_elements(*ShopPage.cardTitles)

    def getFooterButtons(self):
        return self.driver.find_elements(*ShopPage.footerButtons)

    def getCheckoutButton(self):
        return self.driver.find_element(*ShopPage.checkoutButton)
