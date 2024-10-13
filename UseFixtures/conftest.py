import pytest
from selenium import webdriver


@pytest.fixture(params=("chrome", "edge", "firefox"))
def setup_and_tear(request):
    global driver
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "edge":
        driver = webdriver.Edge()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.google.com/en")
    request.cls.driver = driver
    yield
    driver.quit()
