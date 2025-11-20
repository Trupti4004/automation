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

#subcontractor process
sub = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sub-Contractor Process']"))
)
sub.click()

#Create
wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
create = wait.until(
    EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Create']"))
)
create.click()

#Process name
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
pn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='txtName']"))
)
pn.clear()
pn.click()
pn.send_keys("casting")

# HSN code
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
hsn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@role='combobox']"))
)
hsn.click()
hsn.send_keys("25")

# Service Account Code
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
sac = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@role='combobox'])[2]"))
)
sac.click()
sac.send_keys("99")

wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
service = wait.until(
    EC.element_to_be_clickable((By.XPATH,"(//span[@class='ng-arrow-wrapper'])[2]"))
)
service.click()

#Applicable Type
applicable_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='drpAppType']//input[@role='combobox']")))
applicable_input.send_keys("Mac")
time.sleep(1)

wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
apply = wait.until(
    EC.element_to_be_clickable((By.XPATH,"(//span[@class='ng-arrow-wrapper'])[3]"))
)
apply.click()

#WIP From Stage
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
from_stage = wait.until(EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='drpWipFromStage']//input[@role='combobox']")))
from_stage.send_keys("fet")
time.sleep(1)

#WIP to stage
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
stageto = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='drpWipToStage']//input[@role='combobox']"))
)
stageto.click()
stageto.send_keys("exte")

#WIP return to stage formcontrolname="drpWipRtnStage"
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
stagertn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//ng-select[@formcontrolname='drpWipRtnStage']//input[@role='combobox']"))
)
stagertn.click()
stagertn.send_keys("shot")

wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
appl = wait.until(
    EC.element_to_be_clickable((By.XPATH,"(//span[@class='ng-arrow-wrapper'])[6]"))
)
appl.click()

#Boring Generated
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
common_rate = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-check-input d-block ng-untouched ng-pristine ng-valid'])[1]"))
)
common_rate.click()

# Common Rate
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
common_rate = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@formcontrolname='IsCommWORate'])"))
)
common_rate.click()

#Contractor Stock
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
contractor = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@formcontrolname='IsContractorStk'])"))
)
contractor.click()

#Remark
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
Remark = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@formcontrolname='txtRemark'])"))
)
Remark.click()
Remark.send_keys("xyz")

#Active material
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
active = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//input[@formcontrolname='IsActiveCode'])"))
)
active.click()

#Submit   Submit
wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])
submit = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//button[normalize-space()='Submit'])"))
)
submit.click()


time.sleep(5)


