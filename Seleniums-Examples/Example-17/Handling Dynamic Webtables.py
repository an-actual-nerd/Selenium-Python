from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(service= Service(EdgeChromiumDriverManager().install()))
driver.get("https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html")
driver.maximize_window()
driver.implicitly_wait(20)

rows = driver.find_elements(By.XPATH, "//*[@id=\"customers\"]/tbody/tr")
# total_rows = print(len(rows))
total_rows = len(rows)

cols = driver.find_elements(By.XPATH, "//*[@id=\"customers\"]/tbody/tr[1]/th")
# total_cols = print(len(cols))
total_cols = len(cols)

# Printing the text in table
for row in rows:
    print(row.text)

print("-----------------Second Way--------------------------")

start_xpath = "//*[@id=\"customers\"]/tbody/tr[1"
mid_xpath = "]/th["
end_xpath = "]/span"

# //*[@id="customers"]/tbody/tr[1]/th[3]/span
# //*[@id="customers"]/tbody/tr[2]/td[1]/span


for col in range(1, total_cols+1):
        print(driver.find_element(By.XPATH, start_xpath + mid_xpath + str(col) + end_xpath).text)

start_xpath1 = "//*[@id=\"customers\"]/tbody/tr["
mid_xpath1 = "]/td["
end_xpath1 = "]/span"

for row in range(2, total_rows+1):
    for col in range(1, total_cols + 1):
        print(driver.find_element(By.XPATH, start_xpath1 + str(row) + mid_xpath1 + str(col) + end_xpath1).text)


driver.quit()