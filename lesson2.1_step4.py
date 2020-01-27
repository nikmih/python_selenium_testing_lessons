from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/math.html")

try:
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    option1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()