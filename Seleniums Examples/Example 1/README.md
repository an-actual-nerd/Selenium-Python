# What is Web driver

Web driver is an automation framework that helps to send commands to the browser.
It helps to manupulate DOM events.

# Webdriver download.

For selenium to communicate to browser, it need browser executable file.
Each browser provider has it's know browser executable file. 

[Browser Executable File](https://www.selenium.dev/downloads/)
Go to browser section and download the file.

<b>Note- Make sure version of file should be same as browser.</b>

# Launching browser script

1) Importing webdriver from selenium
```commandline
from selenium import webdriver
```
2) Importing service class to tarting and stopping of
    `msedgedriver`
```commandline
from selenium.webdriver.edge.service import Service
```
3) Assignig a variable for webdriver path were it is stored.
4) Assign an variable for Edge browser.
```commandline
edge_path = "Selenium-learning/Webdriver File/msedgedriver.exe"  # Webdriver path
service = Service(executable_path= edge_path)
driver = webdriver.Edge(service= service)
```

# Some basic driver function
1) Navigation to any website.
2) Maximizing the browser window.
3) Go get the title of the website
4) Close to exit current running window.
5) Quite to exit whole session.
```commandline
driver.get("Website link")
driver.maximize_window()
title = driver.title
print(title)
driver.close()
driver.quit()
```

# Assertion in title
Find the text in the title. Mentioned the name/text to find in the title.
```commandline
assert "<>" in title
```
If no text is present in title, there will be an assertion error.

# Full Code
```commandline
from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_path = "Selenium-learning/Webdriver File/msedgedriver.exe"  # Webdriver path
service = Service(executable_path= edge_path)
driver = webdriver.Edge(service= service)

driver.get("https://www.google.com/")
driver.maximize_window()

title = driver.title
print(title)

assert "Google" in title

driver.close()
driver.quit()
```