import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Setup Edge driver
service = Service(r"C:\webdrivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("http://192.168.1.156/MachEasy/auth/login")

# --- Login ---
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").clear()
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("12345")
driver.find_element(By.ID, "remember-check").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# company
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
first_company = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='col ng-star-inserted'])[1]"))
)
first_company.click()

# system
system = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ul[@id='side-menu']/li[2]/a"))
)
system.click()

# Production configuration
pc = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ul[@class='sub-menu ng-star-inserted mm-collapse mm-show']/li[1]/a[1]"))
)
pc.click()

# Machine Shop-Operation (click to expand submenu)
operation = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//ul[@class='sub-sub-menu ng-star-inserted mm-collapse mm-show']/li[1]/a[1]"))
)
operation.click()

submenu_items = driver.find_elements(By.XPATH, "//ul[@class='sub-sub-menu ng-star-inserted mm-collapse mm-show']/li/a")

# Print all submenu texts
print("Submenu items under Machine Shop-Operation:")

for item in submenu_items:
    if item.text.strip() == "Shift":
        item.click()
        print("Clicked on Shift submenu.")
        break
else:
    print("'Shift' submenu not found.")

time.sleep(5)  # For demo purposes to see the result

