import requests
from lxml.html import fromstring, tostring

response = requests.get('http://www.khan.co.kr/')

html = fromstring(response.content)
elements = html.xpath('//div[@class="sectionB"]//strong[@class="hd_title top"]/a')

for element in elements:
    title = element.text
    if title == None:
        title = element.xpath('./font')[0].text
    print('title:', title)
    print(element.get('href'))