from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))
driver.get("https://demo.automationtesting.in/Slider.html")
driver.implicitly_wait(10)
driver.maximize_window()

slide_bar_option1 = driver.find_element(By.XPATH, "//*[@id=\"slider\"]")

# Find the location and the size.
main_slider = driver.find_element(By.ID, "slider")
location = main_slider.location
size = main_slider.size
print(location)
w, h = size["width"], size["height"]
print(size)
print(w,h)
ActionChains(driver).drag_and_drop_by_offset(slide_bar_option1, 10, 0).perform()


driver.quit()