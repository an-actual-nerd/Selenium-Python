from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))

driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()
driver.implicitly_wait(1)

driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/button").click()
alert = Alert(driver)
print(alert.text)
time.sleep(3)
alert.accept()

time.sleep(10)
driver.quit()