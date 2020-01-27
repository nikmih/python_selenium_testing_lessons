import os
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector("[name= 'firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[name= 'lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[name= 'email']")
    input3.send_keys("IPerov@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    inputfile = browser.find_element_by_id("file")
    inputfile.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(10)
    browser.quit()