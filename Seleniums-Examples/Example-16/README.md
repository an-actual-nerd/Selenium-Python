# Handling Javascript Function

• Javascript function can directly can be called in Selenium.

• **execute_script** is used to synchronously executes JavaScript in the current window/frame.

```commandline
driver.execute_script('return document.title;')
```

# Full Source Code
```commandline
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_onsubmit")
driver.maximize_window()
driver.implicitly_wait(20)

driver.switch_to.frame("iframeResult")
ele = driver.find_element(By.XPATH, "/html/body/form/input[1]").send_keys("Gaurav")
driver.execute_script("myFunction()")

time.sleep(5)
driver.quit()
```