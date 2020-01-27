from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[for='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    time.sleep(10)
    browser.quit()