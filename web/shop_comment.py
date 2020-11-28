import requests as req
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

from fake_useragent import UserAgent
import time

# 브라우저의 옵션을 사용하는 방법
options = Options()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

browser = webdriver.Chrome("D:\IJH\chromedriver.exe")
browser.get("http://itempage3.auction.co.kr/DetailView.aspx?itemno=B674702537#vip_tab_comment")

try:
    # soupDocument = bs(response.text,"html.parser")
    WebDriverWait(browser, 10).\
        until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'li#tap_moving_2')))

    review = browser.find_element_by_css_selector('li#tap_moving_2 a')
    review.click()

except Exception as e:
    print(e)
    # browser.quit()

   
# browser.quit()
