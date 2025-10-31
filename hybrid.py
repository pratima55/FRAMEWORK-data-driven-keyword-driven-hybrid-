from selenium import webdriver
from selenium.webdriver.common.by import By
import csv, time

def perform_action(keyword, locator, value, data):
    #Replace placeholders with real test data
    value = value.format(**data) if value else None
    element = driver.find_element(By.ID, locator)


    if keyword == "enterText":
        element.send_keys(value)
    elif keyword == "click":
        element.click()


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

#Read test data (loop over users)
with open("testdata.csv") as datafile:
    datareader = csv.DictReader(datafile)
    for data in datareader:
        #For each user, run keyword steps
        with open("keywords.csv") as keyfile:
            keyreader = csv.DictReader(keyfile)
            for row in keyreader:
                perform_action(row["keyword"], row["locator"], row["value"], data)


        time.sleep(2)
        driver.get("https://www.saucedemo.com/") 



driver.quit()               