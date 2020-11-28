# 중앙일보의 기사 목록

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from bs4 import BeautifulSoup

import requests
import time

# 크롬 웹드라이버를 이용한 브라우저 객체를 생성

browser = webdriver.Chrome('d:\\IJH\\chromedriver.exe')
browser.set_window_size(800, 400)

# 중앙일보의 메인 페이지로 이동
browser.get('https://joongang.joins.com/')

WebDriverWait(browser, 10) \
                       .until( EC.presence_of_element_located(
                           (By.CSS_SELECTOR, 'div.type1 ul.list_vertical a')))

# 메인 페이지의 소스 가져오기 
# src = browser.page_source
# soupDocument = BeautifulSoup(src, 'html.parser')

# 메인 페이지의 기사 목록을 가져오기
newses = browser.find_elements_by_css_selector('div.type1 ul.list_vertical a')
time.sleep(2)

for news in newses:
    news.click() # 뉴스 페이지로 이동

    WebDriverWait(browser, 10) \
                       .until( EC.presence_of_element_located(
                           (By.CSS_SELECTOR, 'p.content')))
    
    comments = browser.find_elements_by_css_selector('p.content')
    time.sleep(2)
    
    for comment in comments:
        print(comment.text)

    
    comments.clear() # 브라우저의 기존 내용을 지워준다.
    browser.back()
    time.sleep(5)
    



# selenium 이용해서 요소 가져오기
# element = browser.find_element_by_css_selector('div.type1 ul.list_vertical a')
# element.click()

# 댓글 가져오기
# comment_area = browser.find_element_by_class_name('comment_area')
# print(comment.text)

# comment = browser.find_element_by_css_selector('p.content')
# comment.text

# selenium의 페이지 로딩 대기
# 특정 요소가 페이지에 로딩 될 때까지 대기
# WebDriverWait
# WebDriverWait(dirver, 시간(초)).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'CSS_RLE')))



















