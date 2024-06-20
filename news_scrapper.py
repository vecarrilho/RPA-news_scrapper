import time
import xlsxwriter
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

url = "https://www.aljazeera.com/search/"
new_url = url + 'trump'
new_url = new_url + '?sort=date'
# new_url = new_url + '?sort=relevance'

driver.get(new_url)

# wait for page to load
element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//button[@class='show-more-button grid-full-width']")))
# print(element.is_displayed())

# Click show more to load more news
# show_more_button = driver.find_element(By.XPATH, "//button[@class='show-more-button grid-full-width']")
# show_more_button.click()

# Write the informations into the worksheet
# workbook = xlsxwriter.Workbook('planilha.xlsx')
# worksheet = workbook.add_worksheet("Minha Planilha")

# worksheet.write('A1', 'Nome')
# worksheet.write('B1', 'Idade')
# worksheet.write('A2', 'João')
# worksheet.write('B2', 25)

# workbook.close()

time.sleep(10)