import time
from selenium import webdriver

link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fields = [browser.find_element_by_xpath('//label[contains(text(), "First name*")]/following-sibling::input'),
              browser.find_element_by_xpath('//label[contains(text(), "Last name*")]/following-sibling::input'),
              browser.find_element_by_xpath('//label[contains(text(), "Email*")]/following-sibling::input')]

    #    fields = browser.find_elements_by_xpath('//input[@required]')

    for field in fields:
        field.send_keys("bla")

    button = browser.find_element_by_xpath("//button[text()=\"Submit\"]")
    button.click()
    time.sleep(2)
    welcome_text_elt = browser.find_element_by_tag_name('h1')
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(5)

finally:
    time.sleep(10)
    browser.quit()
