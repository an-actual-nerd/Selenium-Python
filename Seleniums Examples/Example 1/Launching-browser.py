from selenium import webdriver
from selenium.webdriver.edge.service import Service

edge_path = "Selenium-learning/Webdriver File/msedgedriver.exe"
service = Service(executable_path= edge_path)
driver = webdriver.Edge(service= service)