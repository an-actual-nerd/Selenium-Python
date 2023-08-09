from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))
driver.get("https://demo.applitools.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element(By.XPATH, "/html/body/div/div/form/div[3]/div[1]/label/input").click()

time.sleep(4)
driver.quit()