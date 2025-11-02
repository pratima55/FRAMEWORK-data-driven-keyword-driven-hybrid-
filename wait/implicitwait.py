from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#Implicit wait
driver.implicitly_wait(5)

driver.get("https://www.amazon.com")

#Find search box and type
search = driver.find_element(By.ID, "twotabsearchtextbox")
search.send.keys("laptop")

#click search button
driver.find_element(By.ID, "nav-search-submit-button").click()

print("Implicit wait success!")

driver.quit()