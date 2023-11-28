# Handling Right Click

• It is performed using function called "context_click" from Actionschains.
```commandline
context_click(on_element: WebElement | None = None)
```
• on_element: The element to context-click. If None, clicks on current mouse position.

• First finding the xpath of the web element
```commandline
img = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]/img")
```

• Using context_click
```commandline
ActionChains(driver).context_click(img).perform()
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

driver.get("https://deluxe-menu.com/popup-mode-sample.html")
driver.implicitly_wait(1)
driver.maximize_window()

img = driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/div[2]/table[1]/tbody/tr/td[3]/p[2]/img")

ActionChains(driver).context_click(img).perform()

time.sleep(10)
driver.quit()
```