# Handling drag and drop

• Actions chanins are again used for darg and drop elements.

• First finding draggable element.
```commandline
draggable = driver.find_element(By.ID, "draggable")
```
• Second find the droppable element.
```commandline
droppable = driver.find_element(By.ID, "droppable")
```

• Using action chains to drag and drop method
```commandline
drag_and_drop(source: WebElement, target: WebElement) → ActionChains
```
• source: The element to mouse down.

• target: The element to mouse up.
```commandline
ActionChains(driver).drag_and_drop(draggable, droppable).perform()
```

# Full Source Code

```commandline
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))

driver.get("https://jqueryui.com/resources/demos/droppable/default.html")
driver.maximize_window()
driver.implicitly_wait(1)

draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

ActionChains(driver).drag_and_drop(draggable, droppable).perform()

time.sleep(10)
driver.quit()
```