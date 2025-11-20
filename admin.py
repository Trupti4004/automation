import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException, TimeoutException

# ----------------------------

# Setup Chrome driver

# ----------------------------

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://192.168.1.156/MachEasy/auth/login")

wait = WebDriverWait(driver, 20, poll_frequency=1, ignored_exceptions=[NoSuchElementException])

# ----------------------------

# Login

# ----------------------------

driver.find_element(By.ID, "username").clear()

driver.find_element(By.ID, "username").send_keys("admin")

driver.find_element(By.CSS_SELECTOR, "input[type='password']").clear()

driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys("12345")

driver.find_element(By.ID, "remember-check").click()

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

# ----------------------------

# Navigate to Sub-Contractor Process

# ----------------------------

first_company = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='col ng-star-inserted'])[1]")))

first_company.click()

system = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@id='side-menu']/li[3]/a")))

system.click()

pc = wait.until(EC.element_to_be_clickable(

    (By.XPATH, "//ul[@class='sub-menu ng-star-inserted mm-collapse mm-show']/li[1]/a[1]")))

pc.click()

operation = wait.until(EC.element_to_be_clickable(

    (By.XPATH, "//ul[@class='sub-sub-menu ng-star-inserted mm-collapse mm-show']/li[1]/a[1]")))

operation.click()

sub = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Sub-Contractor Process']")))

sub.click()

create = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Create']")))

create.click()

# ----------------------------

# Enter Process Name

# ----------------------------

pn = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='txtName']")))

pn.clear()

pn.send_keys("casting")


# ----------------------------

# Reusable function for ng-select dropdown

# ----------------------------

def select_ng_dropdown(formcontrolname, value_to_select):
    """

    Selects a value from ng-select dropdown using formcontrolname and visible text.

    """

    try:

        # Click dropdown

        dropdown = wait.until(EC.element_to_be_clickable(

            (By.XPATH, f"//ng-select[@formcontrolname='{formcontrolname}']")))

        dropdown.click()

        time.sleep(0.5)

        # Type value in search box

        search_input = wait.until(EC.element_to_be_clickable(

            (By.XPATH, f"//ng-select[@formcontrolname='{formcontrolname}']//input[@role='combobox']")))

        search_input.clear()

        search_input.send_keys(value_to_select)

        time.sleep(0.5)

        # Select exact match

        option = wait.until(EC.element_to_be_clickable(

            (By.XPATH,
             f"//ng-select[@formcontrolname='{formcontrolname}']//div[contains(@class,'ng-option')]/span[text()='{value_to_select}']")))

        option.click()

        time.sleep(0.5)

    except TimeoutException:

        print(f"ERROR: Value '{value_to_select}' not found in dropdown '{formcontrolname}'")


# ----------------------------

# Fill Dropdowns

# ----------------------------

select_ng_dropdown("drpChapter", "25081090  25081090")  # HSN Code

select_ng_dropdown("drpServiceAcNo", "99 TRANSPORT  SERVICE")  # Service Account Code

select_ng_dropdown("drpAppType", "Machining Process With Item")  # Applicable Type

# ----------------------------

# Example: If you want to fill WIP From / To / Return stages

# ----------------------------

# select_ng_dropdown("drpWipFromStage", "FETTLING SHOP")

# select_ng_dropdown("drpWipToStage", "EXTERNAL MACHINE SHOP")

# select_ng_dropdown("drpWipRtnStage", "FETTLING SHOP")

# ----------------------------

# Done - click Submit

# ----------------------------

submit_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']")))

submit_btn.click()

print("Form submitted successfully!")

