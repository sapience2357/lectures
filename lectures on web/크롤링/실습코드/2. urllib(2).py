import urllib.request as request
# import urllib.error as error
# from urllib.error import URLError, HTTPError
from urllib.error import *

# urlopen() 라이브러리 함수의 사용법

image = "https://learningspoons.com/wp-content/uploads/2018/07/%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5-min.jpg"

# urllib에서 제공되는 urlretrieve를 통해 다운로드를 했다면 ... 
# urllib에서 제공되는 urlopen()를 사용해보죠 

response = request.urlopen(image) 

print('response-line: {} {}'.format(response.status, response.reason))
binaryImage = response.read() # 이미지의 원본(바이너리)

# 그냥 쓰기모드('w')로 파일을 오픈하면 텍스트 형태의 파일로 저장이 된다. 
with open('./download/AIimage.jpg', 'wb') as file:
    file.write(binaryImage)