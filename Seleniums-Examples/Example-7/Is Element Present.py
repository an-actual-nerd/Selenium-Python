from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchDriverException

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(1)

# def element_present_by(ID):
#     try:
#         driver.find_elements(By.ID, ID)
#         return True
#     except NoSuchDriverException:
#         return False
#
# print(element_present_by("user-name"))

def element_present_by(how, what):
    try:
        driver.find_elements(by= how, value= what)
        return True
    except NoSuchDriverException:
        return False

print(element_present_by(By.ID, "user-name")) # ID can be replacec by Xpath or any other locator