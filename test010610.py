import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
try:

    browser.get(link)

#    button = browser.find_element_by_css_selector("button.btn")
#    fields = browser.find_elements_by_xpath('//label[contains(text(), "name*") or contains(text(), "Email*")]'
#                                            '/following-sibling::input')
    fields = browser.find_elements_by_xpath('//input[@required]')

    for field in fields:
        field.send_keys("bla")
    button = browser.find_element_by_xpath("//button[text()=\"Submit\"]")
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text
#    print(browser.switch_to_alert().text)
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)

finally:
    time.sleep(10)
    browser.quit()
