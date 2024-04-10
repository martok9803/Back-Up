from selenium import webdriver
from selenium.webdriver.common.by import By  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("http://192.168.200.20/gui/monitor/dashboard")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("admin")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("evrista_pass359")

sign_in_button = driver.find_element(By.XPATH, "//button[.//span[text()='SIGN IN']]")
sign_in_button.click()

wait = WebDriverWait(driver, 20)
configure_menu = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "configureIcon"))
)
configure_menu.click()

firmware = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/gui/configure/firmware')]"))
)
firmware.click()

backup_restore_tab = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@data-tag='backup']"))
)
backup_restore_tab.click()

apply_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-apply"))
)
apply_button.click()

modal_apply_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "modal-apply-button"))
)
modal_apply_button.click()

time.sleep(20)

driver.quit()
