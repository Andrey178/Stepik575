import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

#    button = browser.find_element_by_css_selector("button.btn")
    fields = browser.find_elements_by_xpath('//input')
    for field in fields:
        field.send_keys("bla")
    button = browser.find_element_by_xpath("//button[text()=\"Submit\"]")
    button.click()
#    print(browser.switch_to_alert().text)
    time.sleep(10)
    print(browser.switch_to_alert().text)



finally:
    time.sleep(10)
    browser.quit()
