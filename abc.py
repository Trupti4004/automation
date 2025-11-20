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

#company
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
first_company = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='col ng-star-inserted'])[1]"))
)
first_company.click()

#jobwork
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
menu_item = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ul[@id='side-menu']/li[1]/a[1]"))
)
menu_item.click()
time.sleep(5)

#order acceptance
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
oa = wait.until(
    EC.element_to_be_clickable((By.XPATH,"//ul[@class = 'sub-menu ng-star-inserted mm-collapse mm-show']/li[1]/a[1]"))
)
oa.click()

#OA operation
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
operation = wait.until(
    EC.element_to_be_clickable((By.XPATH,"//ul[@class='sub-sub-menu ng-star-inserted mm-collapse mm-show']/li[1]/a"))
)
operation.click()

#amendment
'''wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
amend = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//ul[@class='sub-sub-menu ng-star-inserted mm-collapse mm-show']/li[2]/a"))
)
amend.click()'''

wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
create = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,"//div[@class='col-12 d-flex flex-wrap justify-content-start gap-2']/button[1]/i[1]")))
create.click()


time.sleep(5)
