# 매우 간단한 클라이언트 소켓 프로그래밍
# 접속할 서버의 주소는 www.sundooedu.co.kr
# 접속할 서버의 포트는 80

import socket

# 도메인 이름을 ip주소로 변경
serverIpAddress = socket.gethostbyname('www.sundooedu.co.kr')
serverPortNumber = 80

# TCP 통신을 하기 위한 소켓을 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 생성된 소켓을 통해서 서버에 연결
# OSI 7 Layer의 하위 4계층의 내용을 자동으로 구성
sock.connect(
    # 접속할 서버의 정보는 튜플 형태로 전달
    (serverIpAddress, serverPortNumber)
)

# www.sundooedu.co.kr 기본 페이지를 요청하는 헤더
request_header = 'GET / HTTP/1.1\r\n'
request_header += 'Host: www.sundooedu.co.kr\r\n' # 헤더 필드
request_header += '\r\n'

sock.send(request_header.encode())
response = sock.recv(1024)
print(
    'received:',
    response.decode()
)

# 통신이 끝나면 소켓을 정리 
sock.close()