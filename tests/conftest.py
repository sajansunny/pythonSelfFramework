import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")