# lxml 라이브러리의 사용
# xml 분석용

import requests
import lxml.html

# requests 라이브러리를 통해서 대상 페이지를 불러옵시다. 
# 일간 스포츠의 프로야구 기사 목록

response = requests.get('http://isplus.live.joins.com/news/list/list.asp')

html = lxml.html.fromstring(response.content)

isPlusUrls = []
# for anchor in html.cssselect('a.title_cr'):
    # print(anchor.get('href'))
    # isPlusUrls.append(anchor.get('href'))

# xpath를 사용한 문서 구조 가져오기(스크래핑)
# 크롤링(Crawling Vs. Scraping)
# //*[@id="news_list"]/div[2]/ul/li[1]/dl/dt/a

# elements = html.xpath('//*[@id="news_list"]/div[2]/ul/li[1]/dl/dt/a')
elements = html.xpath('//a[@class="title_cr"]')

for element in elements:
    print('title:', element.text)
    print('url:', element.get('href'))