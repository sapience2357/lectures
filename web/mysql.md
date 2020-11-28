# 1. 파이썬에서 DBMS관련 라이브러리 사용
- mysql DBMS를 사용
- 1. 페이스북이나, 인스타, 뉴스 등의 댓글을 수집해서 저장(텍스트 데이터를 저장) - 영문
- 2. openAPI를 이용해서 데이터를 수집, 저장(json, xml 파싱 하는법)

## 1.1. 구름 컨테이너에서 mysql server를 실행하는 방법

```
    #> mkdir -p /var/run/mysqld
    #> ls -ld /var/run/mysqld
    drwxrwxr-x 2 root root 4096 11월 25 00:26 /var/run/mysqld/

    #> chown mysql:mysql /var/run/mysqld
    #> ls -ld /var/run/mysqld
    drwxrwxr-x 2 mysql mysql 4096 11월 25 00:26 /var/run/mysqld/

    #> mysqld_safe &
    ... blar blar ~~~ ... <enter>

    #> netstat -ant
    ...
    tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN
    ...

    #> ps -ef | grep mysqld_safe
    ...
    root        2289     236  0 00:27 pts/1    00:00:00 /bin/sh /usr/bin/mysqld_safe

    #> mysql -u root
    ...
    mysql>


```   

## mysql 관련 명령어

- 데이터베이스 목록 확인
```
    mysql> SHOW DATABASES;
```   

- 데이터베이스 생성   
```
    mysql> CREATE DATABASE SDAcademy;
```   

- 데이터베이스 삭제   
```
    mysql> DROP DATABASE SDAcademy;
```   

- 데이터베이스 사용   
```
    mysql> USE SDAcademy;
```   

## mysql 사용자 패스워드 변경및 설정    

```
    mysql> use mysql;
    mysql> SELECT Host, User, authentication_string FROM user;
    +-----------+------------------+-------------------------------------------+
    | Host      | User             | authentication_string                     |
    +-----------+------------------+-------------------------------------------+
    | localhost | root             |                                           |
    | localhost | mysql.session    | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
    | localhost | mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
    | localhost | debian-sys-maint | *7B1145654083926C439BFF8877986ED2813026C6 |
    +-----------+------------------+-------------------------------------------+

    mysql> UPDATE user SET authentication_string = password('1234') WHERE User='root';
    mysql> SELECT Host, User, authentication_string FROM user;
    +-----------+------------------+-------------------------------------------+
    | Host      | User             | authentication_string                     |
    +-----------+------------------+-------------------------------------------+
    | localhost | root             | *A4B6157319038724E3560894F7F932C8886EBFCF |
    | localhost | mysql.session    | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
    | localhost | mysql.sys        | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE |
    | localhost | debian-sys-maint | *7B1145654083926C439BFF8877986ED2813026C6 |
    +-----------+------------------+-------------------------------------------+

    mysql> FLUSH PRIVILEGES;
```


## mysql 관련 사용자 추가 설정    

```
    mysql> use mysql;
    mysql> SELECT Host, User, plugin FROM user;
    +-----------+------------------+-----------------------+
    | Host      | User             | plugin                |
    +-----------+------------------+-----------------------+
    | localhost | root             | socket...             |
    | localhost | mysql.session    | mysql_native_password |
    | localhost | mysql.sys        | mysql_native_password |
    | localhost | debian-sys-maint | mysql_native_password |
    +-----------+------------------+-----------------------+

    mysql> UPDATE user SET plugin="mysql_native_password" WHERE User='root';
    mysql> SELECT Host, User, plugin FROM user;
    +-----------+------------------+-----------------------+
    | Host      | User             | plugin                |
    +-----------+------------------+-----------------------+
    | localhost | root             | mysql_native_password |
    | localhost | mysql.session    | mysql_native_password |
    | localhost | mysql.sys        | mysql_native_password |
    | localhost | debian-sys-maint | mysql_native_password |
    +-----------+------------------+-----------------------+

    mysql> FLUSH PRIVILEGES;

```


# 댓글 수집

## 1. 신문사 등의 사이트를 이용해서 뉴스 목록을 수집