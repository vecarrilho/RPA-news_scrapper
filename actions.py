from sema4ai.actions import action


@action
def news_scrapper(search_sentence: str, topic: str) -> str:
    """
    Search LA Times news.

    Args:
        search_sentence (str): The sentence that will be search in LA Times
        topic (str): The topic to filter the search in LA Times [World & Nation, Opinion, Politics, Sports, Business]

    """

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

    url = "https://www.latimes.com/search"

    list = []

    driver.get(url)

    # Search the inputs in the driver
    search_input = driver.find_element(By.XPATH, "//input[@class='search-results-module-input']")
    search_input.click()
    search_input.send_keys(search_sentence)
    search_topic = driver.find_element(By.XPATH, "//label[@class='checkbox-input-label']//span[text()='"+topic+"']")
    search_topic.click()
    button_submit = driver.find_element(By.XPATH, "//button[@class='button submit-button']")
    button_submit.click()

    time.sleep(5)

    # Find all the NEWS
    lis_raw = driver.find_elements(By.XPATH, "//ul[@class='search-results-module-results-menu']//li")
    count = len(lis_raw)

    # Populate the object with the variables
    for i in range(0, count):
        count_phrases = 0

        # Save the variables of each NEWS
        title = lis_raw[i].find_element(By.XPATH, ".//h3[@class='promo-title']//a[@class='link']")
        description = lis_raw[i].find_element(By.XPATH, ".//div[@class='promo-content']//p[@class='promo-description']")
        date = lis_raw[i].find_element(By.XPATH, ".//div[@class='promo-content']//p[string-length(@data-timestamp)>0]").get_attribute("data-timestamp")
        try:
            image = lis_raw[i].find_element(By.XPATH, ".//picture//img[@class='image']").get_attribute("alt")
        except NoSuchElementException:
            image = 'This file does not contain a filename'

        try:
            image_src = lis_raw[i].find_element(By.XPATH, ".//picture//img[@class='image']").get_attribute("src")
        except NoSuchElementException:
            image_src = 'This file does not contain a SRC'

        count_phrases = title.text.count(search_sentence)
        count_phrases += description.text.count(search_sentence)
        list.append((title.text, description.text, date, image, count_phrases, False, image_src))
        
        continue

    # Create a Excel File with the informations
    df = pd.DataFrame(list, columns=['title', 'description', 'date', 'image_filename', 'count_phrases', 'has_money', 'image_src'])
    df.to_excel('planilha.xlsx')

    return "Sentence searched"