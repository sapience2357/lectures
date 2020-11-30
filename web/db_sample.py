import pymysql as db

conn = db.connect(
    host = 'localhost',        # 접속할 mysql 서버의 주소
    user = 'root',             # 접속할 mysql 서버의 계정(리눅스 시스템 계정 x)
    password = '1234',        # 접속할 mysql 서버의 계정 패스워드
    db = 'SDAcademy',         # mysql 서버에 접속한 이후 사용 할 데이터베이스
    charset = 'utf8'
)

# cur = conn.cursor()
cur = conn.cursor(db.cursors.DictCursor)

query = "SELECT Host, User FROM mysql.user"
numOfRows = cur.execute(query)

rows = cur.fetchall()
for row in rows:
    print(row)