from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, '.container .nowrap:nth-child(2)')
    x = x_element.text
    
    y_element = browser.find_element(By.CSS_SELECTOR, '.container .nowrap:nth-child(4)')
    y = y_element.text
    
    sum = int(x) + int(y)     
      
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(sum))    

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(10)
    browser.quit()
