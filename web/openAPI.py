import requests
import urllib.parse

key = "9Td+AysuLzv3Fq4/SIhE/ri4rGiZiFjD92SQxmfQalI/2vW3xPEOcSNURc+LUMqpgZoCrTL8gD1mXFb1QhXBIg=="
endPoint = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

values = {
    'ServiceKey': key,
    'sidoName': '서울',
    'ver': '1.3',
    'numOfRows': '10',
    'pageNo': '1'
}

params = urllib.parse.urlencode(values)
endPoint = endPoint + '?' + params

print(endPoint)
response = requests.get(endPoint)
print(response.text)





