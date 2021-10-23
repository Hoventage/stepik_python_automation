import os

from selenium import webdriver as driver
from selenium.webdriver.common.by import By

base_url = 'http://suninjuly.github.io/file_input.html'
browser = driver.Chrome()

try:
    browser.get(base_url)

    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    first_name.send_keys('Pete')
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    last_name.send_keys('Petrov')
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys('qwe@qwe.qwe')

    file_upload_button = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_data.txt')
    file_upload_button.send_keys(file_path)

    submit_button = browser.find_element(By.TAG_NAME, 'button')
    submit_button.click()


finally:
    browser.quit()




