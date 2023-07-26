from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.select import Select
import time

driver =  webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))

driver.get("https://echoecho.com/htmlforms11.htm")
driver.maximize_window()
driver.implicitly_wait(20)

# driver.find_element(By.NAME, "dropdownmenu").send_keys("Cheese")
dropdown = driver.find_element(By.NAME, "dropdownmenu")
select  = Select(dropdown) # Accepts your web-element
select.select_by_visible_text("Cheese")

time.sleep(5)
driver.quit()