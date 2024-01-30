# Webdriver Integration

• Web driver integration is a combination of using both seleniunm and pytest to create a tescase.

• Imports
```commandline
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import pytest
```
• We will use the same code that we have used in parametrize marker example (Example-5) with slight changes.

• Selenium is used in setup function and teardown function.

```commandline
def setup_function():
    global driver
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://facebook.com")
    driver.maximize_window()

def teardown_function():
    driver.quit()
```

# Full Code

```commandline
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import pytest

def get_data():
    return [
        ("me@automation.com", "12345789"),
        ("you@automation.com", "87654321"),
        ("python@automation.com", "003456")
    ]

def setup_function():
    global driver
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    driver.get("https://facebook.com")
    driver.maximize_window()

def teardown_function():
    driver.quit()

@pytest.mark.parametrize("username, password", get_data())
def test_login(username, password):
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys(username)
    driver.find_element(By.XPATH, "//input[@name='pass']").send_keys(password)

```