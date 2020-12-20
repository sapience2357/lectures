import requests
import lxml.html

response = requests.get("https://news.joins.com/article/23921624?cloc=joongang-home-toptype1basic")

html = lxml.html.fromstring(response.content)

# selector = '.comment_area .bd .comment_list .list .item .cmt_info dd p.content'
selector = '#comment'

elements = html.cssselect(selector)

for element in elements:
    print(lxml.html.tostring(element))