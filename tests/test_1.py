import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test1:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.saucedemo.com/')
        yield
        self.driver.quit()


    # driver.find_element(By.ID, "user-name").send_keys("standard_user")
    # driver.find_element(By.ID, "password").send_keys("secret_sauce")
    def test_click_login_btn(self,setup):
        self.driver.find_element(By.ID, "login-button").click()
        assert self.driver.current_url == 'https://www.saucedemo.com/', "Página alterada!"

        error_msg = self.driver.find_element(By.CLASS_NAME, 'error-message-container').text
        assert error_msg == 'Epic sadface: Username is required', 'Mensagem de erro não encontrada'
        time.sleep(3)


