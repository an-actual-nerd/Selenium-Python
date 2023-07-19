from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

edge_path = "Selenium-learning/Webdriver File/msedgedriver.exe"  # Webdriver path
service = Service(executable_path= edge_path)

driver = webdriver.Edge(service= service)

# It is an online automation testing website. Web element of writing username is used for this code,
driver.get("https://identity.telerik.com/sign-up?redirect_uri=https:%2F%2Fwww.telerik.com%2Ftracking%2Flogin%3Fredirect_uri%3Dhttps%253a%252f%252fwww.telerik.com%252faccount%252f&response_type=code&client_id=http:%2F%2Fwww.lean.telerik.com.v2&state=5E8A37E91D0C14DF8D740AC1237EECB8966195146680AB3647C4FF48A01FE655")
driver.maximize_window()
driver.implicitly_wait(20)

time.sleep(15)
driver.find_element(By.ID, "email").send_keys("Selenium@python.com")
driver.find_element(By.XPATH, "//*[@id='registerForm']/div[2]/button").click()
driver.find_element(By.ID, "password").send_keys("Learning")


time.sleep(5) #Adding a delay
driver.quit()