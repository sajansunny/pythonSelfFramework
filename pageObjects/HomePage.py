from selenium.webdriver.common.by import By
from pageObjects.ShopPage import ShopPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")
    name = (By.XPATH, "//input[@name='name']")
    email = (By.XPATH, "//input[@name='email']")
    password = (By.XPATH, "//input[@type='password']")
    icecreamLover = (By.XPATH, "//input[@id='exampleCheck1']")
    gender = (By.CSS_SELECTOR, "select.form-control")
    employmentStatus = (By.XPATH, "//input[@name='inlineRadioOptions']")
    dob = (By.XPATH, "//input[@name='bday']")
    submit = (By.CSS_SELECTOR, "input.btn-success")
    alert = (By.CSS_SELECTOR, "div.alert-success")

    def shop_link(self):
        self.driver.find_element(*HomePage.shop).click()
        shop_page = ShopPage(self.driver)
        return shop_page

    def getNameTextbox(self):
        return self.driver.find_element(*HomePage.name)

    def getEmailTextbox(self):
        return self.driver.find_element(*HomePage.email)

    def getPasswordTextbox(self):
        return self.driver.find_element(*HomePage.password)

    def getIcecreamLoverCheckbox(self):
        return self.driver.find_element(*HomePage.icecreamLover)

    def getGenderDropdown(self):
        return self.driver.find_element(*HomePage.gender)

    def getEmploymentStatusRadio(self):
        return self.driver.find_element(*HomePage.employmentStatus)

    def getDOBDate(self):
        return self.driver.find_element(*HomePage.dob)

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit)

    def getAlertText(self):
        return self.driver.find_element(*HomePage.alert).text


