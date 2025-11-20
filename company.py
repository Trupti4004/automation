import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.common.exceptions import NoSuchElementException

service = Service(r"C:\webdrivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("http://192.168.1.156/MachEasy/auth/login")

# Login
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"input[type='password']").clear()
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("12345")
driver.find_element(By.ID, "remember-check").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# Explicit wait for the first company element to be clickable
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
first_company = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='col ng-star-inserted'])[1]"))
)

company = driver.find_element(By.XPATH, "(//div[@class='col ng-star-inserted'])[1]")
company.click()

from selenium.webdriver.support.ui import Select

# Wait until the element is clickable
menu_item = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//ul[@id='side-menu']/li[1]/a[1]")
    )
)

# Click the menu item (Job Work or first menu)
menu_item.click()


# Click the first company
first_company.click()



