from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
#
# try:
#     browser = webdriver.Chrome('H:\chromedriver.exe')
#     browser.get('https://www.taobao.com')
#     input = browser.find_element_by_id('q')
#     input.send_keys('iPhone')
#     time.sleep(1)
#     input.clear()
#     input.send_keys('iPad')
#     button = browser.find_element_by_class_name('btn-search')
#     button.click()
# finally:
#     browser.close()