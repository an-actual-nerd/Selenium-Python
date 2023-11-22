# Handling Resizable Element

• Change the size of the resizable element using ActionChains.

• This is performed by first finding the xpath.
```commandline
drag_and_drop_by_offset(source: WebElement, xoffset: int, yoffset: int)
```
• source: The element to mouse down.

• xoffset: X offset to move to.

• yoffset: Y offset to move to.

# Process

• Locate the xpath of slider. Pass is to the action chanins in drag.

# Full Source Code

```commandline
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))

driver.get("https://jqueryui.com/resources/demos/resizable/default.html")
driver.maximize_window()
driver.implicitly_wait(1)

resizable = driver.find_element(By.XPATH, "//*[@id=\"resizable\"]/div[3]")
ActionChains(driver).drag_and_drop_by_offset(resizable, 800, 400).perform()

time.sleep(10)
driver.quit()
```