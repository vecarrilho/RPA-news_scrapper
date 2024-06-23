import time
import xlsxwriter
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
url = "https://www.g1.com.br"
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
# element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[@class='show-more-button grid-full-width']")))
# print(element.is_displayed())

search_input = driver.find_element(By.XPATH, "//input[@id='busca-campo']")
search_input.click()
search_input.send_keys('trump')
search_input.submit()

lis_raw = driver.find_elements(By.XPATH, "//li[@class='widget widget--card widget--info']")
count = len(lis_raw)

# Populate the object with the variables
for i in range(0, count):
    title = lis_raw[i].find_element(By.XPATH, ".//div[@class='widget--info__title product-color ']")
    description = lis_raw[i].find_element(By.XPATH, ".//p[@class='widget--info__description']")
    date = lis_raw[i].find_element(By.XPATH, ".//div[@class='widget--info__meta']")
        
    try:
        image = lis_raw[i].find_element(By.XPATH, ".//a[@class='widget--info__media ']//img").get_attribute("src")
    except NoSuchElementException:
        image = ''

    try:
        video = lis_raw[i].find_element(By.XPATH, ".//a[@class='widget--info__media widget--info__media--video']//img").get_attribute("src")
    except NoSuchElementException:
        video = ''
    
    if image == '' and video == '':
        image_src = ''
    elif image == '':
        image_src = video
    elif video == '': 
        image_src = image

    # news = News(title.text, description.text, date.text, image_src, 2, True)

    list.append((title.text, description.text, date.text, image_src, 2, True))
    
    continue

df = pd.DataFrame(list, columns=['title', 'description', 'date', 'image_sr', 'count_phrases', 'has_money'])
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