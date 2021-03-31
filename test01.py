import time
from selenium import webdriver

#from selenium.webdriver.chrome.options import Options
#import webdriver_manager

#caps = webdriver.DesiredCapabilities.CHROME.copy()
#caps['start-maximized'] = False
#caps['window-size'] = [300, 200]

options = webdriver.ChromeOptions()
options = webdriver.FirefoxOptions()
#options.binary_location = 'Chromepath'
#chrome_driver_binary = 'Chromedriverpath'
#browser = webdriver.Chrome(desired_capabilities=caps)
#browser = webdriver.chrome(chrome_driver_binary, chrome_options = options)
#browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver/geckodriver')
browser = webdriver.Firefox()
time.sleep(10)
browser.get('http://seleniumhq.org/')
time.sleep(20)
browser.get('http://ya.ru/')
#time.sleep(40)
for i in reversed(range(40)):
    print(i)
    time.sleep(1)
browser.quit()
