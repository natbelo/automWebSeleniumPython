import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')


# driver.find_element(By.ID, "user-name").send_keys("standard_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
assert driver.current_url == 'https://www.saucedemo.com/', "Página alterada!"

error_msg = driver.find_element(By.CLASS_NAME, 'error-message-container').text
assert error_msg == 'Epic sadface: Username is required', 'Mensagem de erro não encontrada'
time.sleep(3)
