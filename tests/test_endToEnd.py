import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.usefixtures("setup")
class TestOne:
    def test_endToEnd(self):


        product_names = driver.find_elements_by_xpath("//h4[@class='card-title']")
        for product_name in product_names:
            if product_name.text == "Blackberry":
                product_name.find_element_by_xpath("parent::div/parent::div/div[2]/button").click()
                break
        driver.find_element_by_xpath("//a[@class = 'nav-link btn btn-primary']").click()
        driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        driver.find_element_by_xpath("//input[@id='country']").send_keys("Ind")
        wait = WebDriverWait(driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        driver.find_element_by_link_text("India").click()

        checkbox = driver.find_element_by_xpath("//input[@id='checkbox2']")
        driver.execute_script("arguments[0].click();", checkbox)
        driver.find_element_by_xpath("//input[@type='submit']").click()
        assert "Thank you" in driver.find_element_by_class_name("alert-success").text
        driver.get_screenshot_as_file("endToEnd.png")
        driver.close()
