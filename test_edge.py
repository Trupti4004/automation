import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Give full path of your driver
service = Service(r"C:\webdrivers\edgedriver_win64\msedgedriver.exe")

# Launch Microsoft Edge
driver = webdriver.Edge(service=service)

# Open Google
driver.get("https://www.google.com")

print("Page Title:", driver.title)

time.sleep(10)
