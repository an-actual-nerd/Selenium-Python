# Handling sliders

• Drag and drop by offset from ActionChains is used to handle sliders.

• This method firstly performs a click-and-hold on the source element, moves to the given offset and then releases the mouse.
```commandline
ActionChains(driver).drag_and_drop_by_offset(self, source, xoffset, yoffset).perform()
```
• Xoffset= Value to traverse the slider in x-axix

• Yoffset- Value to traverse the slider in y-axix
# Process 

• Locate the xpath of slider. Pass is to the action chanins.

# Full source code

```commandline
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
```
