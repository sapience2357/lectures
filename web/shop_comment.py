import requests as req
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.firefox.options import Options

from fake_useragent import UserAgent
import time

# 브라우저의 옵션을 사용하는 방법
# options = Options()
options = webdriver.ChromeOptions()
options.add_argument("-headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# browser = webdriver.Firefox(executable_path="./geckodrer", options=options)
browser = webdriver.Chrome(executable_path= './chromedriver', options=options)

response = req.get("http://corners.auction.co.kr/AllKill/AllDay.aspx")
soupDocument = bs(response.text, "html.parser")
itemList = soupDocument.select("ul.item_list div.inner > a")

for item in itemList:

    try:
        browser.get(item['href'])
        WebDriverWait(browser, 10).\
            until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'li#tap_moving_2')))

        review = browser.find_element_by_css_selector('li#tap_moving_2 a')
        review.click()

    except Exception as e:
        print(e)
        browser.quit()


    soupHTML = bs(browser.page_source, "html.parser")
    commentList = soupHTML.select("ul.list__review li.list-item div.box__review-text > p")
    
    for comment in commentList:
        print(comment.get_text())
        
    time.sleep(10)

# with open('./download/shop_by_html_source.html', 'w') as file:
    # file.write(soupHTML.prettify())
    
browser.quit()
