from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))

driver.get("https://www.google.com")



'''
driver.implicitly_wait(10)

search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("selenium")
googlesearch_button = driver.find_element(By.NAME,"btnK")
googlesearch_button.click()'''
'''
wait = WebDriverWait(driver,10)

search_box = wait.until(EC.visibility_of_element_located((By.NAME,"q")))
search_box.send_keys("Explicit Wait")

googlesearch_button = wait.until(EC.element_to_be_clickable((By.NAME,"btnK")))
googlesearch_button.click()'''

wait = WebDriverWait(driver,10,poll_frequency=0.3,ignored_exceptions=[NoSuchElementException])


search_box = wait.until(EC.visibility_of_element_located((By.NAME,"q")))
search_box.send_keys("Fluent Wait")

googlesearch_button = wait.until(EC.element_to_be_clickable((By.NAME,"btnK")))
googlesearch_button.click()


driver.quit()