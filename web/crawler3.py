import requests
# from requests import *

# url = 'https://news.google.com'
# ret = get(url)
# ret = requests.get(url)
data = {
    'user_id': 'azazel02',
    'password': 'password',
    's_url': '/'
}

response = requests.post('https://www.ppomppu.co.kr/zboard/login_check.php?s_url=/', 
                            data=data)
print(response.content.decode(encoding='euc-kr'))