from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.wikipedia.org/")

links = driver.find_elements(By.TAG_NAME, "a")

# To print all the links of a webpage
for link in links:
    print("Text is:", link.text, "--URL is:", link.get_attribute("href"))

# Print a selective link
print("First link:", links.__getitem__(0).text)

time.sleep(10)
driver.close()
