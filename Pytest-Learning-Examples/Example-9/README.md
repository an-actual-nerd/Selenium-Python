# Generating Allure report

• In previous example we have generated HTML report, in this example we will generate another HTML report using allure.

### What is Allure

• Allure is a test reporting tool, provides clear graphical reports.
https://allurereport.org/docs/

### Downloading Allure and setting up allure
• Download the latest one https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.27.0/

• Setting up allure in environment variables https://www.skill2lead.com/allure-report/allure-report-behave-allure-report-configuration.php

• After following above steps install allure in pycharm from settings(Settings -> Interpreter -> add allure pytest)

### Generating allure files

• Create a folder for allure reports (allure_reports).

• To create json file
```commandline
pytest test_(file name).py --alluredir= "allure file directory name that made from above point"
```

• After the above command being executed Json file would have been created in that allure directory.

• To generate allure report tyoe in cmd
```commandline
alluer serve <allure file directory>
```

# Full source code

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
    driver.find_element(By.XPATH,
                        "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys(
        username)
    driver.find_element(By.XPATH, "//input[@name='pass']").send_keys(password)
```