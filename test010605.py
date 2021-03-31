import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_link_text"
number = str(math.ceil(math.pow(math.pi, math.e) * 10000))
print(number)
try:
    browser = webdriver.Chrome()
    browser.get(link)

    input0 = browser.find_element_by_link_text(number)
    print(input0.get_attribute("href"))
    time.sleep(15)
#    browser.get(input0.get_attribute("href"))
    input0.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    print(browser.switch_to_alert().text)
    time.sleep(2)
    browser.switch_to_alert().accept()



finally:
    time.sleep(10)
    browser.quit()
