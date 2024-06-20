import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
# options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("start-maximized") 

driver = webdriver.Chrome(options=options)

driver.get("https://www.aljazeera.com/")

# wait for page to load
# element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//button//span[contains(text(), 'Click here to search')]")))
# time.sleep(5)
# print(element.is_displayed())

search_field = driver.find_element(By.XPATH, "//span[contains(text(), 'Click here to search')]/ancestor::button")
search_field.click()
# search_field.send_keys('teste')
# time.sleep(5)

# print(element)