from selenium import webdriver
from selenium.webdriver.common.by import By
import time

broweser = webdriver.Chrome()
broweser.get("http://suninjuly.github.io/registration1.html")
fields = broweser.find_elements(By.CSS_SELECTOR, 'form .first_block > * input')

try:
    first = broweser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    first.send_keys('placeholder')

    second = broweser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    second.send_keys('placeholder')

    third = broweser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    third.send_keys('placeholder')

    button = broweser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    button.click()

    time.sleep(1)
    succ_alert = broweser.find_element(By.TAG_NAME, 'h1').text
    print(succ_alert)
    assert "Congratulations! You have successfully registered!" == succ_alert

finally:
    time.sleep(1)
    broweser.quit()
