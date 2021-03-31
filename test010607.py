import time
from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fields = browser.find_elements_by_tag_name("input")
    for field in fields:
        field.send_keys("bla")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
#    print(browser.switch_to_alert().text)
    time.sleep(10)
    print(browser.switch_to_alert().text)



finally:
    time.sleep(10)
    browser.quit()
