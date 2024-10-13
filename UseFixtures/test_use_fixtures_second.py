import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup_and_tear')
class TestYuvraj:
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_yuvraj_page(self):
        exp_title = 'Google'
        actual_title = self.driver.title
        assert actual_title.__eq__(exp_title)
        self.driver.find_element(By.NAME, 'q').send_keys('Yuvraj')
        self.driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]').click()
        expected_result = 'Yuvraj Singh'
        actual_result = self.driver.find_element(
            By.XPATH, '//*[@id="rcnt"]/div[2]/div/div/div[3]/div/div[1]/div/div/div[2]/div[1]/div/div').text
        assert expected_result.__eq__(actual_result)
        time.sleep(2)
        allure.attach(self.driver.get_screenshot_as_png(),name='test_yuvraj_page',attachment_type=AttachmentType.PNG)
