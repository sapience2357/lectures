import requests
import urllib.parse

# 한국환경공단 대기오염정보

# 요청할 URL
# openAPI는 이러한 URL 형태로 제공된다.
endpoint = "http://openapi.airkorea.or.kr/openapi/services\
/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"

# 서비스 키는 공공데이터 포털의 마이페이지, 혹은
# 한국환경공단_대기오염정보 페이지에서 확인 가능
# 복사해서 붙여넣읍시다.
serviceKey = "9Td+AysuLzv3Fq4/SIhE/ri4rGiZiFjD92SQxmfQalI/2vW3xPEOcSNURc+LUMqpgZoCrTL8gD1mXFb1QhXBIg=="

# 매개변수 셋팅 1.
# 시도별 실시간 측정정보 조회
# sidoName = 조회하고 싶은 도시
# ver = 조회하고자 하는 오퍼레이션 버전
# serviceKey = 발급받은 인증키 
# _returnType = 응답 메시지 형태(json, xml)
# 매개변수의 순서는 상관이 없습니다. 
# endpoint = "http://openapi.airkorea.or.kr/openapi/services/\
# rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName={}&\
# ver={}&_returnType={}&ServiceKey={}".format('서울', '1.3', 'json', serviceKey)

# GET parameter(매개변수)
# 파이썬의 dict 타입을 사용하여 전달할 매개변수를 구성
values = {
    # key(변수명): value,
    'sidoName': '서울',
    'ver': '1.3',
    '_returnType': 'json',
    'ServiceKey': serviceKey,
}

param = urllib.parse.urlencode(values)

endpoint = endpoint + '?' + param
print(endpoint)

response = requests.get(endpoint)
statusCode = response.status_code

if statusCode == 200:
    print(response.text)
else:
    print('Receive failed')