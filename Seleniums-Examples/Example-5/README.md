# Handling Dropdown List
• Drop downs in a website could be created in several different ways. 

• Some dropdowns are dynamic in nature which means after clicking or selecting any option, the drop downs values would populate accordingly.

• Drop down is always an **Select** tag. Option inside drop down list must be in **Option**" tag.
### One way it can be handled by "send_keys" function.
```commandline
driver.find_element(By.NAME, "dropdownmenu").send_keys("Cheese")
```
• Find the drop down list by name and send keys.
• Cheese will get selected in drop down list.

• "send_keys" function can create problems sometimes because of duplicacy.

## There is a dedicated way to handle drop downlist.
• We can import **Select**
```commandline
from selenium.webdriver.support.select import Select
```

```commandline
dropdown = driver.find_element(By.NAME, "dropdownmenu")
select  = Select(dropdown) # Accepts your web-element
select.select_by_visible_text("Cheese")
```

# Full Source Code
```commandline
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.select import Select
import time

driver =  webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))

driver.get("https://echoecho.com/htmlforms11.htm")
driver.maximize_window()
driver.implicitly_wait(20)

# driver.find_element(By.NAME, "dropdownmenu").send_keys("Cheese")
dropdown = driver.find_element(By.NAME, "dropdownmenu")
select  = Select(dropdown) # Accepts your web-element
select.select_by_visible_text("Cheese")

time.sleep(5)
driver.quit()
```