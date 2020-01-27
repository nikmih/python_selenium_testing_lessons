from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

try:
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    sum = str(int(x)+int(y))
    select = Select (browser.find_element_by_id("dropdown"))
    select.select_by_value(sum)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
     
finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()