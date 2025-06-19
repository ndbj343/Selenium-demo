import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class")
def setup(request):
    # Set up the MAIN driver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 15)
    driver.implicitly_wait(3)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    request.cls.wait = wait

    yield
    driver.quit()