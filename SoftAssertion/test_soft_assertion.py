import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_soft_assersion():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/en")
    exp_title = 'Googles'
    actual_title = driver.title
    assert actual_title.__eq__(exp_title)
    driver.find_element(By.NAME, 'q').send_keys('Sachin')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
    driver.find_element(By.XPATH,
                        '//*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div[1]/div/div').is_displayed()
    time.sleep(2)
    driver.quit()

"""
run the program with the command 'pytest file_location --soft-asserts', this way run all code and execute all asserts
even if any of the assert getting fails.
"""

