# WebDriverManager Library and configuration more browser
• Previously we have to download browser executable file manually.

• This process can be get automated.

• Can be done by downloading a library called **Webdriver manager**

• Go to terminal and type.
```commandline
 pip install webdriver-manager
```
**Note- Make sure virtual environment is running**

### Importing webdriver manager
```commandline
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
```

# Full Code
```commandline
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

driver.get("https://www.google.com/")
driver.maximize_window()

title = driver.title
print(title)

assert "Google" in title

time.sleep(5) #Adding a delay
driver.close()
driver.quit()
```