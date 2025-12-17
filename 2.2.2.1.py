from selenium import webdriver
import time

try:
    
    browser = webdriver.Chrome()
    browser.execute_script('document.title="Script executing";')
    
finally:

    time.sleep(10)
    browser.quit()