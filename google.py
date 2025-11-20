from selenium import webdriver
import time
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

service = Service(r"C:\webdrivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Enter name
driver.find_element(By.NAME, "name").send_keys("Sakshi")

# Enter email
driver.find_element(By.NAME, "email").send_keys("sakshi@example.com")

# Enter password
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")


driver.find_element(By.ID,"exampleCheck1" ).click()

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

dropdown.select_by_visible_text("Female")

time.sleep(10)

