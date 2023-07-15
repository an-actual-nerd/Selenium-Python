from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

edge_path = "Selenium-learning/Webdriver File/msedgedriver.exe"  # Webdriver path
service = Service(executable_path= edge_path)
driver = webdriver.Edge(service= service)

driver.get("https://www.google.com/")
driver.maximize_window()

title = driver.title
print(title)

assert "Google" in title

time.sleep(5) #Adding a delay
driver.close()
driver.quit()