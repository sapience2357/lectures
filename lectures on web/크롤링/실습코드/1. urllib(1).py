# urllib
import urllib.request as request
import urllib.error as error

# html 문서와 그림 파일 정도 다운로드 받아보도록 하죠 ... 
# 그림 파일도 저작권 없는 걸로 ... 

# 그림 파일 
imageUrl = "https://dthezntil550i.cloudfront.net/mz/latest/mz1907231329049290009566440/1280_960/20bac9b4-fe7c-4c7b-b5a6-0e4e3fe5b546.png"

# html 문서(naver main)
htmlUrl = "http://www.naver.com/"

# 예외처리는 예외가 발생할 것 같은 코드를 try에 넣어줍니다. 
try:
    filePath, http = request.urlretrieve(htmlUrl, './download/download_document.html')
except error.HTTPError as e:
    print('ERROR: ', e.code)
except Exception as e:
    print(e)

print('download file name:', filePath)
