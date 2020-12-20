# BeautifulSoup 라이브러리 활용법

# 실습용 HTML 파일이 필요
# 매번 다운로드 할 수는 없으니 파일 형태로 저장 후
# 파일을 불러와서 적용

# html 파일을 저장
# 1. urllib.request.urlretrieve(그림, html, 파일, ... )
# 2. urllib.request.urlopen
# 3. requests

import urllib.request as request
import requests
from bs4 import BeautifulSoup

'''
documentUrl = "https://ko.wikipedia.org/wiki/%EA%B8%B0%EA%B3%84_%ED%95%99%EC%8A%B5"
downloadPath = "D:\IJH\sample.html"

try:    
    request.urlretrieve(documentUrl, downloadPath)
except Exception as e:
    print(e)
'''
filePath = "D:\IJH\sample.html"
# 실습용 html 문서를 불러오기
with open(filePath, 'r', encoding='utf-8') as file:
    document = file.read()

# package 설치
# > pip list
# ...

# > pip install package_name

# 불러온 html 문서에 beautifulSoup을 적용
# BeautifulSoup 객체로 변환
# print(type(document))
# soupDoc = BeautifulSoup(document, 'html.parser')
# print(type(soupDoc))

# find, find_all 메소드 사용

# 찾고자 하는 태그를 검색할 때 사용
soupDoc = BeautifulSoup(document, 'html.parser')
h1 = soupDoc.find('h1')
print(h1)

div = soupDoc.find('div')
print(div)

# 특정 조건으로 검색하고 싶은 경우
div = soupDoc.find('div', id='siteNotice')
print(div)

# 특정 조건을 여러개 두고 싶은 경우
condition = {
    'class': 'noprint'
}
div = soupDoc.find_all('div', attrs=condition)
# print(div)

# find Vs. find_all
# 조건에 맞는 태그를 전부 찾거나,
# 처음 매칭 되는 태그를 찾거나의 차이

# find_all은 결과를 리스트 형태로 돌려준다.

for element in div:
    print(element)


# 검색한 태그의 value를 추출
# 자식 요소가 있는 경우와 없는 경우

h1 = soupDoc.find('h1')
print(h1.get_text())
print(h1['lang'])   # 속성값 추출

div = soupDoc.find('div', id='content')
print(div.get_text())


# (선택자) select_one, select
# CSS 선택자를 통해 요소를 선택
# lxml과 유사한 접근 방법

# id 속성의 값을 이용한 선택
div = soupDoc.select_one("div#content")
print(div)

# 자식 요소를 선택
anchor = soupDoc.select_one('div#content > a')
print(anchor)

# 요소의 속성을 이용한 선택
h1 = soupDoc.select_one('h1[lang="ko"]')
print(h1)


div = soupDoc.select('div.noprint')
print(div)























    


