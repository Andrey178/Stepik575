import math
import time
from selenium import webdriver


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element_by_xpath("//button").click()
    browser.switch_to.window(browser.window_handles[1])

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x_element = str(math.log(abs(12 * math.sin(int(x_element.text)))))

    #    browser.find_element_by_xpath("//select").click()
    #    browser.find_element_by_xpath("//option[@value='{}']".format(x)).click()

    #    elements = ["//input[@id='robotCheckbox']", "//input[@id='robotsRule']", "//button[text()=\"Submit\"]"]

    browser.find_element_by_xpath("//input[@id='answer']").send_keys(x_element)

    browser.find_element_by_css_selector("button.btn").click()
    #    fields = browser.find_elements_by_xpath('//label[contains(text(), "name*") or contains(text(), "Email*")]'
    #                                            '/following-sibling::input')
    time.sleep(12)
    print(browser.switch_to.alert.text)
#    welcome_text_elt = browser.find_element_by_tag_name('h1')
#    welcome_text = welcome_text_elt.text
#    print(browser.switch_to_alert().text)
#    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()
