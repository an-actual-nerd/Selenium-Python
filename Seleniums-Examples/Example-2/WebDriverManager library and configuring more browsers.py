from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get("https://www.google.com/")
driver.maximize_window()

title = driver.title
print(title)

assert "Google" in title

time.sleep(5) #Adding a delay
driver.close()
driver.quit()