import requests as req
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from fake_useragent import UserAgent

import time

headers = {
    'User-Agent': UserAgent().chrome
}

response = req.get(
    "https://joongang.joins.com/",
    headers = headers
)
soupDocument = bs(response.text,"html.parser")

# 뉴스 목록
urls = soupDocument.select(
    'div.type1 ul.list_vertical a:nth-child(1)'
)

#for url in urls:
#    print(url['href'])

# 뉴스 본문

chrome_driver = 'D:\IJH\chromedriver.exe'
browser = webdriver.Chrome(chrome_driver)


for url in urls:
    browser.get(url['href'])

    # comment_list 요소가 로딩 될 때까지 대기

    # WebDriverWait(browser, 10).\
    # until(EC.presence_of_element_located(
    #    (By.CSS_SELECTOR, '.comment_list')))

    src = browser.page_source

    soupComment = bs(src, "html.parser")

    comments = soupComment.select( 'div.comment_list \
    ul.list p.content')

    for comment in comments:
        print(comment.get_text())

    time.sleep(300)











