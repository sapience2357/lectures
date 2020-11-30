# 매우 간단한 클라이언트 소켓 프로그래밍
# 접속할 서버의 주소는 vortex.labs.overthewire.org
# 접속할 서버의 포트는 5842

import socket
import struct

serverIpAddress = '176.9.9.172'
serverPortNumber = 5842

# TCP 통신을 하기 위한 소켓을 생성
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 생성된 소켓을 통해서 서버에 연결
# OSI 7 Layer의 하위 4계층의 내용을 자동으로 구성
sock.connect(
    # 접속할 서버의 정보는 튜플 형태로 전달
    (serverIpAddress, serverPortNumber)
)

# 연결된 소켓을 통해서 서버로부터 데이터를 수신
# 변수 = sock.recv(수신할 데이터의 크기)
number1 = sock.recv(4)
number2 = sock.recv(4)
number3 = sock.recv(4)
number4 = sock.recv(4)

number1 = struct.unpack('<I', number1)[0] 
number2 = struct.unpack('<I', number2)[0]
number3 = struct.unpack('<I', number3)[0]
number4 = struct.unpack('<I', number4)[0]

print(
    number1, number2, number3, number4
)

# 시스템이 사용하는 byte order와 
# 네트워크 통신에서 사용하는 byte order가 
# 다르기 때문에
total = number1 + number2 + number3 + number4
print('total:', total)
total = struct.pack('<Q', total) # byte order를 다시 조정

# 생성된 소켓을 통해서 데이터를 송신
sock.send(total)

# 생성된 소켓을 통해서 데이터를 수신
data = sock.recv(1024)
print(
    'received:',
    data.decode()
)

# 통신이 끝나면 소켓을 정리 
sock.close()