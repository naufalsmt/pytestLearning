import allure
import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures('setup_and_tear')
class TestSachinGanguly:
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sachin_page(self):
        exp_title = 'Google'
        actual_title = self.driver.title
        assert actual_title.__eq__(exp_title)
        self.driver.find_element(By.NAME, 'q').send_keys('Sachin')
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
        expected_rslt ='Sachin Tendulkar'
        actual_rslt = self.driver.find_element(
            By.XPATH, '//*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div[1]/div/div').text
        assert expected_rslt.__eq__(actual_rslt)
        time.sleep(2)

    @allure.severity(allure.severity_level.MINOR)
    def test_ganguly_page(self):
        exp_title = 'Google'
        actual_title = self.driver.title
        assert actual_title.__eq__(exp_title)
        self.driver.find_element(By.NAME, 'q').send_keys('Ganguly')
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
        expected_rslt = 'Sourav Ganguly'
        actual_rslt = self.driver.find_element(
            By.XPATH, '//*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[1]/div').text
        assert expected_rslt.__eq__(actual_rslt)
        time.sleep(2)
