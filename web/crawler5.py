import requests
# import lxml.html
from lxml.html import fromstring, tostring

# requests의 GET 메서드를 이용해 네이버의 메인 페이지를 가져오자. 
response = requests.get('http://www.naver.com')

# 가져온 네이버의 메인 페이지의 html 소스코드를 lxml 객체 형태로 변환
# html = lxml.html.fromstring(response.content)
html = fromstring(response.content)

# cssselect를 이용해서 원하는 요소를 뽑아보자. 
#for anchor in html.cssselect('.sc_newscast .tile_view a.btn_popup'):
#    dataClick = anchor.get('data-clk')
#    if dataClick == 'logo':
#        print(anchor.get('href'))

# xpath를 이용해서 동일한 요소에 접근 
# /    : css selector의 '>'와 같은 의미, 하위요소(직계)
# //   : css selector에서 ' '와 같은 의미 
# @    : 속성을 지정할 때 사용
# *: wildcard(대체문자: ?, ., ) 정규표현식(regular expression)
    
# elements = html.xpath(
#    '//*[@id="NM_NEWSSTAND_DEFAULT_THUMB"]/div[1]/div/div[@class="tile_view"]/\
#    div[@class="thumb_area"]/div/div/a[3]'
# )

elements = html.xpath(
    '//div[@id="newsstand"]//div[@class="tile_view" and @class="another"]//a[@class="btn_popup"]'
)
for element in elements:
    print(element.get('href'))
