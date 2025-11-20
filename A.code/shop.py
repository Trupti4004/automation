import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Setup Edge driver
driver = webdriver.Chrome()

driver.get("http://192.168.1.156/macheasy/auth/login")

# --- Login ---
driver.find_element(By.ID, "username").clear()
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR, "input[type='password']").clear()
driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("12345")
driver.find_element(By.ID, "remember-check").click()
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

#company
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
first_company = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='building-icon-section'])"))
)
first_company.click()

company = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='continue-section ng-star-inserted'])"))
)
company.click()

#system
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
system = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ul[@id='side-menu']/li[4]/a"))
)
system.click()

#Production configuration
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
pc = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ul[@class='sub-menu ng-star-inserted mm-collapse mm-show']/li[1]/a[1]"))
)
pc.click()

#Machine shop operation
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
operation = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ul[@class='sub-sub-menu ng-star-inserted mm-collapse mm-show']/li[1]/a[1]"))
)
operation.click()

#Operation
operation = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Shop']"))
)
operation.click()

#Create
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
create = wait.until(
    EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Create']"))
)
create.click()

#Shop name
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
optnm = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='txtName']"))
)
optnm.click()
optnm.send_keys("casting")

#Submit
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
submit = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Submit'])"))
)
submit.click()

time.sleep(2)

