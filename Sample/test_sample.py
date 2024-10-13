import time
from selenium import webdriver


def test_open_google():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://google.com")
    time.sleep(5)
    driver.quit()


def test_open_arada():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://arada.com/en/")
    time.sleep(5)
    driver.quit()


def test_open_hugrywolves():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://hungrywolves.ae/en/")
    time.sleep(5)
    driver.quit()


def test_open_yallawheels():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://yallawheels.com/en/")
    time.sleep(5)
    driver.quit()


def test_open_zad():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.visitzad.com/en/")
    time.sleep(5)
    driver.quit()
