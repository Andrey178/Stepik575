import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser.get(link)
    x_element = browser.find_element_by_xpath("//img[@valuex]")
    x = x_element.get_attribute('valuex')
    print(x)
    y = calc(x)
    browser.find_element_by_xpath("//input").send_keys(y)
    browser.find_element_by_xpath("//input[@id='robotsRule']").click()
    browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
#    button = browser.find_element_by_css_selector("button.btn")
#    fields = browser.find_elements_by_xpath('//label[contains(text(), "name*") or contains(text(), "Email*")]'
#                                            '/following-sibling::input')

    button = browser.find_element_by_xpath("//button[text()=\"Submit\"]")
    button.click()
    time.sleep(12)
    print(browser.switch_to_alert().text)
#    welcome_text_elt = browser.find_element_by_tag_name('h1')
#    welcome_text = welcome_text_elt.text
#    print(browser.switch_to_alert().text)
#    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
