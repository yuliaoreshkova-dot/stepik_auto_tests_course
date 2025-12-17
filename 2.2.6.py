from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

driver = webdriver.Chrome()

driver.get("https://suninjuly.github.io/file_input.html")

input1 = driver.find_element(By.NAME, "firstname")
input1.send_keys("Ivan")
input2 = driver.find_element(By.NAME, "lastname")
input2.send_keys("Petrov")
input3 = driver.find_element(By.NAME, "email")
input3.send_keys("test@test.mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element = driver.find_element(By.NAME, "file")
element.send_keys(file_path)

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(10)
# закрываем браузер после всех манипуляций
driver.quit()

# не забываем оставить пустую строку в конце файла