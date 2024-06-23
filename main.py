import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

options = Options()
# options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("start-maximized") 

driver = webdriver.Chrome(options=options)

# url = "https://www.aljazeera.com/search"
url = "https://www.latimes.com/search"
# new_url = url + 'trump'
# new_url = new_url + '?sort=date'
# new_url = new_url + '?sort=relevance'

list = []

class News:
    def __init__(self, title, description, date, filename, count_search_phrase, has_money):
        self.title = title
        self.description = description
        self.date = date
        self.filename = filename
        self.count_search_phrase = count_search_phrase
        self.has_money = has_money

driver.get(url)

# wait for page to load
# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='search-results-module-input']")))

search_value = input('Search Phrase: ')
search_input = driver.find_element(By.XPATH, "//input[@class='search-results-module-input']")
search_input.click()
search_input.send_keys(search_value)
button_submit = driver.find_element(By.XPATH, "//button[@class='button submit-button']")
button_submit.click()

time.sleep(5)

# element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='search-results-module-results-menu']//li")))
lis_raw = driver.find_elements(By.XPATH, "//ul[@class='search-results-module-results-menu']//li")
count = len(lis_raw)

# Populate the object with the variables
for i in range(0, count):
    title = lis_raw[i].find_element(By.XPATH, ".//h3[@class='promo-title']//a[@class='link']")
    description = lis_raw[i].find_element(By.XPATH, ".//div[@class='promo-content']//p[@class='promo-description']")
    date = lis_raw[i].find_element(By.XPATH, ".//div[@class='promo-content']//p[string-length(@data-timestamp)>0]").get_attribute("data-timestamp")
    try:
        image = lis_raw[i].find_element(By.XPATH, ".//picture//img[@class='image']").get_attribute("alt")
    except NoSuchElementException:
        image = ''

    list.append((title.text, description.text, date, image, 2, True))
    
    continue

df = pd.DataFrame(list, columns=['title', 'description', 'date', 'image_filename', 'count_phrases', 'has_money'])
df.to_excel('planilha.xlsx')
# Write the informations into the worksheet
# workbook = xlsxwriter.Workbook('planilha.xlsx')
# worksheet = workbook.add_worksheet("Minha Planilha")

# worksheet.write('A1', 'Nome')
# worksheet.write('B1', 'Idade')
# worksheet.write('A2', 'João')
# worksheet.write('B2', 25)

# workbook.close()

# time.sleep(10)