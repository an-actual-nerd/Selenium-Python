from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

edge_path = "Selenium-learning/Webdriver File/msedgedriver.exe"  # Webdriver path
service = Service(executable_path= edge_path)

driver = webdriver.Edge(service= service)

# It is an online automation testing website. Web element of writing username is used for this code,
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Using locator- ID
# user_name= driver.find_element(By.ID, "user-name")
# user_name.send_keys("Selenium@python.com")
# pass_word = driver.find_element(By.ID, "password")
# pass_word.send_keys("Learning")

driver.find_element(By.ID, "user-name").send_keys("Selenium@python.com")
driver.find_element(By.ID, "password").send_keys("Learning")

# Using locator- xpath
# Using xpath of the login button
driver.find_element(By.XPATH, "//*[@id='login-button']").click()

time.sleep(5) #Adding a delay
driver.quit()