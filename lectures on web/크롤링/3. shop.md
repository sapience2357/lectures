# 수집된 데이터를 DB에 저장하기

## 1. 리눅스에서 selenium 사용하기   

### 단계 1. 리눅스 패키지를 최신 버전으로 업그레이드   
```
    #> apt-get update -y
    ...

    #> apt-get upgrade -y
    ...

```   

- `apt-get`은 데비안 계열의 리눅스 운영체제에서 지원하는 패키지 관리 프로그램
- `yum`은 레드헷 계열의 리눅스 운영체제에서 지원하는 패키지 관리 프로그램   

### 단계 2. 리눅스에서 사용할 브라우저 설치    
- 크롬(설치가 까다로움)
- 파이어폭스(설치가 쉬움)   

```
    #> apt-get firefox -y
    ... 

    #> dpkg -l | grep firefox
    ii  firefox                                83.0+build2-0ubuntu0.18.04.2        amd64
 Safe and easy web browser from Mozilla
```   

- `dpkg` 또한 데비안 계열의 리눅스 운영체제에서 지원하는 패키지 관리 프로그램   


### 단계 3. 파이어폭스용 웹 드라이버 다운로드   

- 우선 `geckodriver`의 다운로드 받을 링크주소를 복사해 옵니다.   
- 구글에서 `geckodriver` 검색후 첫번째 깃허브의 링크로 들어가면 다운로드 가능한 목록 확인 가능
- 가장 최신 버전 파일의 링크를 복사해 옵니다.    

```
    #> wget https://github.com/mozilla/geckodriver/releases/download/v0.28.0/geckodriver-v0.28.0-linux64.tar.gz
    ... 

    #> ls 
    ... geckodriver-v0.28.0-linux64.tar.gz ...

    #> tar xvfz geckodriver-v0.28.0-linux64.tar.gz
    ... 

    #> ls -al geckodriver
    -rwxr-xr-x 1 1000 1000 7932136 11월  3 16:13 geckodriver
```   

- 확장자가 `tar.gz` 으로 된 파일은 압축 파일임을 나타냅니다. 
- 리눅스의 압축은 `tar`와 `gzip`이 합쳐진 명령입니다. 
- 윈도우즈의 압축도 동일한 방식이지만 프로그램이 마치 하나인것 처럼 동작하기 때문에 
- 그렇게 보이지 않을 뿐 동일한 방식 입니다. 
- 리눅스에서의 압축 방식은 크게 `zip`, `gzip`, `bzip`, `Zzip` 등의 형태가 있으며
- 여러개의 파일을 하나로 묶는 방식은 압축이 아닙니다. 
- 리눅스에서는 여러개의 파일을 하나로 묶어주는 방식이 `tar` 입니다. 
- `tar` 명령의 옵션에는 `-`가 붙지 않습니다.


# 우리가 개발자용 커뮤니티를 적극적으로 활용해야 되는 이유(중요)

- 기술의 발전은 너무 빠르고
- 모든 기술에 대한 이슈를 나 혼자 감당하기에는 그 양이 너무 많기 때문에, ... 
- 여러 개발자들이 모여있는 커뮤니티를 적극적으로 활용하지 않으면 
- 금방 뒤쳐지기 때문에, ...

- stackoverflow
- reddit

## DB에 저장하기

### 1. 데이터베이스와 테이블 생성 


#### 1). 한글 인코딩 설정   

- /etc/mysql/mysql.conf.d/mysqld.cnf
```
    ...

    [mysqld]
    ...
    collation-server = utf8mb4_unicode_ci
    character-set-server = utf8mb4
    skip-character-set-client-handshake

    ...
```   

- 설정 추가후 mysqld 재시작   

```
    #> mysqladmin -u root -p shutdown
    #> mysqld_safe &
```


