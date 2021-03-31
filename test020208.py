import time
from selenium import webdriver


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    file_path = "D:\\Programming\\output.txt"

    browser.get(link)
    x_elements = browser.find_elements_by_xpath("//input[@class='form-control']")

    #    browser.find_element_by_xpath("//select").click()
    #    browser.find_element_by_xpath("//option[@value='{}']".format(x)).click()

    #    elements = ["//input[@id='robotCheckbox']", "//input[@id='robotsRule']", "//button[text()=\"Submit\"]"]
    for element in x_elements:
        element.send_keys('bla')

    browser.find_element_by_xpath("//input[@id='file']").send_keys(file_path)


    button = browser.find_element_by_css_selector("button.btn").click()
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
