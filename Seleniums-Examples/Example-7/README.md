# Is Element Present

• Will try to find element using his ID.

• Will create a function.

````commandline
def element_present_by_id(ID):
    try:
        driver.find_elements(By.ID, ID)
        return True
    except NoSuchDriverException:
        return False
````
• We will use **Try** and **Except**.

• To do this we need to import NoSuchDriverException.
```commandline
from selenium.common.exceptions import NoSuchDriverException
```
• Resutls will be **True** if present other wise **False**.

# Full Source Code
```commandline
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchDriverException

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(1)

def element_present_by_id(ID):
    try:
        driver.find_elements(By.ID, ID)
        return True
    except NoSuchDriverException:
        return False

print(element_present_by_id("user-name"))
```

# Catch
• Above code can only find elements with ID.

• What for using other element, Xpath etc, or any other locator.
```commandline
def element_present_by(how, what):
    try:
        driver.find_elements(by= how, value= what)
        return True
    except NoSuchDriverException:
        return False

print(element_present_by(By.ID, "user-name")) # ID can be replacec by Xpath or any other locator
```

# Full Source code
```commandline
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchDriverException

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(1)

def element_present_by(how, what):
    try:
        driver.find_elements(by= how, value= what)
        return True
    except NoSuchDriverException:
        return False

print(element_present_by(By.ID, "user-name")) # ID can be replacec by Xpath or any other locator
```