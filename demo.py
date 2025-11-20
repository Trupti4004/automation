from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service



service = Service(r"C:\webdrivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("http://192.168.1.156/MachEasy/pages/Comm/RoleAccessSel")
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "username").send_keys("ccpl")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").clear()


