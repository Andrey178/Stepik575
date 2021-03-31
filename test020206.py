import time
import math
from selenium import webdriver

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x = int(x_element.text)
    print(x)
    x = math.log(abs(12 * math.sin(x)))

#    browser.find_element_by_xpath("//select").click()
#    browser.find_element_by_xpath("//option[@value='{}']".format(x)).click()
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(str(x))

    elements = ["//input[@id='robotCheckbox']", "//input[@id='robotsRule']", "//button[text()=\"Submit\"]"]
    for element in elements:
        item = browser.find_element_by_xpath(element)
        #item.location_once_scrolled_into_view
        browser.execute_script("return arguments[0].scrollIntoView(true);", item)
        item.click()

#    button = browser.find_element_by_css_selector("button.btn")
#    fields = browser.find_elements_by_xpath('//label[contains(text(), "name*") or contains(text(), "Email*")]'
#                                            '/following-sibling::input')
    time.sleep(12)
    print(browser.switch_to_alert().text)
#    welcome_text_elt = browser.find_element_by_tag_name('h1')
#    welcome_text = welcome_text_elt.text
#    print(browser.switch_to_alert().text)
#    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()
