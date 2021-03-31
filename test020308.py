import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()


try:
    browser.get(link)
    wait = WebDriverWait(browser, 12)
    price = wait.until(ec.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), '$100'))
    #price = wait.until(ec.text_to_be_present_in_element((By.ID, "price"), '$100'))
    browser.find_element_by_xpath("//button[@id='book']").click()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    x_element = str(math.log(abs(12 * math.sin(int(x_element.text)))))
    #    browser.find_element_by_xpath("//select").click()
    #    browser.find_element_by_xpath("//option[@value='{}']".format(x)).click()
    #    elements = ["//input[@id='robotCheckbox']", "//input[@id='robotsRule']", "//button[text()=\"Submit\"]"]
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(x_element)

    button = browser.find_element_by_css_selector("button#solve.btn")
    button.location_once_scrolled_into_view
    button.click()
    #    fields = browser.find_elements_by_xpath('//label[contains(text(), "name*") or contains(text(), "Email*")]'
    #                                            '/following-sibling::input')
    time.sleep(12)
    print(browser.switch_to.alert.text)
#    welcome_text_elt = browser.find_element_by_tag_name('h1')
#    welcome_text = welcome_text_elt.text
#    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    browser.quit()
