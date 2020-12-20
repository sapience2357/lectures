# DBMS

## 1. 관계형 데이터 베이스 

### 1.1. 관계형 DBMS(RDB/Relational DB)
- SQLite
- MySQL
- MariaDB
- Oracle
- ... 

### 1.2. 테이블
- 데이터를 테이블 형태로 저장
- 테이블은 데이터를 저장하는 형태를 규정하는 작업(정규화)
- 테이블은 html의 테이블 혹은 엑셀의 시트와 같은 형태

|col1|col2|col3|...||
|:---:|:---:|:---:|:---:|:---:|
| - | - | - | - | row1 |
| - | - | - | - | row2 |
| - | - | - | - | row3 |

- column은 field, 속성 등의 이름으로 부릅니다. 
- row(행), 자료를 나타내는 record가 되며, 그냥 data 라고도 표현, 혹은 tuple 이라고도 부른다.
- 스키마(schema)는 데이터를 저장하는 테이블의 구조를 나타낸다.

### 2.3. 쿼리(Query)
- SQL(Standard Query Language)

# 2. 실습

## 1. DB(DataBase)
- 데이터를 다루는 단위
- 하나의 DBMS에서 여러 형태의 데이터를 관리
- 환자에 대한 데이터와 직원데 대한 데이터를 분리해서 관리할 필요가 있을 것이다. 
- 환자 DB와 직원 DB를 따로 생성해서 관리해주면 된다.

## 2. table(데이터의 구조)

### 2.1. 문자 타입
- char: char(10)
  - 고정 크기, 속도가 제일 빠르다.
- varchar
  - 최대 크기내에서 가변적
- text
  - 가변적인 크기
- blob
  - 바이너리 형태, 형태가 정의되지 않은 경우

# 3. SQL
- CRUD(Create, Read, Update, Delete): 컴퓨터에서 처리되는 기본적인 기능

## 1. DDL(Data Definition Language): 데이터 정의어

- attributes
```
    NULL/NOT NULL
    PRIMARY KEY
    FOREIGN KEY
    UNIQUE
    AUTOICREMENT
    INTEGER/TEXT/BLOB/REAL, ... 
    DEFAULT
```

- CREATE
```
    CREATE 테이블 이름 (생성) column_name/filed_name attributes, 
    column_name/field_name attributes, 
    ... );
```
- DROP(삭제)
```
    DROP TABLE table_name;
    DROP DATABASE db_name;
```
- ALTER(수정)
```
ALTER TABLE old_table_name RENAME TO new_table_name;
ALTER TABLE table_name RENAME COLUMN old_col_name TO new_col_name 
ALTER TABLE table_name ADD COLUMN new_column_name attributes ...
```

## 2. DML(Data Manipulation Language): 데이터 조작어

### 2.1. 추가(삽입)
```
    -- 테이블에 정의된 컬럼과 순서를 그대로 따르는 경우
    INSERT INTO table_name VALUES(values, ... )
    -- 컬럼과 순서를 선택하는 경우 
    INSERT INTO table_name (columne_name, ... ) VALUES(valuess, ... )
```

### 2.2. 조회 

    - 가장 많이 사용되는 SQL 명령어   


```
    SELECT * FROM table_name;
    SELECT column_name, ... FROM table_name;
    
    -- 조건절 WHERE
    SELECT * FROM table_name WHERE conditions, ...
    SELECT column_name, ...  FROM table_name WHERE conditions, ...
    SELECT * FROM table_name WHERE condition AND|OR condition
    SELECT * FROM table_name WHERE condition &&/|| condition

    -- 정렬 ORDER BY
    SELECT * FROM table_name ORDER BY column_name;
    SELECT * FROM table_name ORDER BY column_name DESC;
    SELECT * FROM table_name ORDER BY column_name ASC;

    -- LIKE 절
    SELECT * FROM tagle_name WHERE phone_number LIKE 검색어;
```
- LIKE절의 '%'는 대체 문자의 역할

### 2.3. 삭제
    - WHERE 절을 사용할 수 가 있다.(SELECT와 동일한 방법)
    - 특정 데이터를 삭제하려면 WHERE절이 필수이다. 
```
    -- 테이블 내의 모든 데이터의 삭제 
    DELETE FROM table_name;

    -- 특정 조건의 데이터만 삭제
    -- 이때, 조건은 primary key, unique 설정이 되어 있는 필드를 
       선택하는 것이 좋다. 
    -- 중복되는 조건에 대해서도 삭제
    DELETE FROM table_name WHERE id=1;
```

### 2.4. 수정

```
    UPDATE table_name SET column_name='value';
    UPDATE table_name SET column_name='value' WHERE condition;
```

## 3. DCL(Data Control Language): 데이터 제어어

- 권한, 트랜잭션, ...



# CSV(Comma Seperated Values)
- 각각의 필드(컬럼)를 콤마로 형태로 구분된 텍스트 파일
- 구분자를 |, tab, space, ;, ...
  - 실제 필드의 값에 콤마가 들어가는 경우
- 엑셀하고는 다름
- 엑셀은 바이너리 형태, 다만 CSV는 엑셀에서 지원 가능한 형태
- 데이터 분석시에 가장 많이 사용되는 형태


# 조회

- 조회시 컬럼명에 대한 별칭   
     
```
SELECT 
	hr as "시간",    
	weathersit as "날씨",    
    windspeed as "풍속",    
	cnt as "자전거 대여수"   
FROM hour WHERE dteday = '2011-01-01';
```   


- 내장함수(sqlite에서 지원하는 함수)
- https://www.sqlite.org/lang_corefunc.html 
- 참조하여 필요한 함수를 사용할 수 있다.   

```
SELECT 
	hr as "시간", 
	weathersit as "날씨", 
	round(windspeed, 2) as "풍속",
	cnt as "자전거 대여수"
	-- sum(cnt) as "자전거 대여수"
FROM hour WHERE dteday = '2011-01-01';
```   

# 뷰(View)

- 가상 테이블   

```
CREATE VIEW myView
AS
SELECT 
	substr(dteday, 1, 4) as "년도",
	substr(dteday, 6, 2) as "월",
	substr(dteday, 9, 2) as "일",
	hr as "시간", 
	temp as "온도", 
	round(windspeed, 2) as "풍속", 
	-- sum(cnt) as "자전거 대여수"
	cnt as "자전거 대여수"
FROM hour WHERE dteday="2011-01-01"
```   

```
    SELECT * FROM myView
```   

- 복잡한 쿼리를 단순화 할 수 있다. 
- 보안상 적합하다.(조회만 가능)
  - DBMS마다 차이가 존재(수정, 삭제가 가능할 수도 있다)


# 인덱스(index)
- 검색을 빠르게 하기 위한 용도로 사용
  - trade-off가 존재하기 때문에, 항상 좋지는 않다.
  - 데이터가 추가 되거나 데이터가 삭제 되는 경우에 index도 동시에 업데이트가 이루어진다.    
  - 데이터의 양이 아주 많으면 인덱스를 업데이트 하는 비용도 많이 발생하기 때문에, 항상 좋지는 않다.    


```
    CREATE INDEX index_name ON table_name( column_name, ... )
```   

- 인덱스를 생성하든 하지않든 검색은 차이가 없다. 
- 그냥 select 쿼리로 조회하면 인덱스가 있는 경우 자동으로 
- 인덱스를 참조할 뿐 ... 
- 그러니깐 그냥 만들어놓고 쓰면 된다. 
- 유니크 속성의 컬럼인 경우 자동으로 인덱스를 생성하는 경우도 있다. 


# 트리거(trigger)
- 방아쇠 같은 의미를 가지고 있어서 
- 어떤 쿼리가 실행된 경우 해당 쿼리에 대한 트리거를 설정 해놓으면
- 쿼리가 방아쇠가 되어서 연쇄적으로 설정된 다른 쿼리를 
- 자동으로 실행   


```
    CREATE TRIGGER trigger_name QUERY{UPDATE, INSERT, DELETE} ON table_name
    BEGIN
        SQL Query
    END;
```   


# 정규 표현식(Regular Expression, regx)
- 문자열을 표현할 수 있는 패턴
- 거의 모든 시스템이 동일한 정규식을 적용   

```
    .       : 임의의 한 문자
    []      : 문자 그룹
    ^       : 라인에서 시작 문자
    [^]     : 부정의 의미를 나타냄
    $       : 라인에서 끝나는 문자
    ()      : 문자열
    *       : 반복(0번이상)
    ?       : 0 또는 1회 매칭
    {}      : 매칭되는 횟수, {min, max}
```   

# 조회 추가

```
/* where 
	부등호도 사용이 가능 
	=: 같다(==)
	<>: 같지 않다.(!=)
	>: 크다 
	<: 작다
	>=: 크거다 같다 
	<=: 작거나 같다 
*/

/*
 * 대체문자: %(여러문자), *(전체 컬럼명, 여러문자), _(문자하나)
*/
-- SELECT * FROM hour WHERE temp > 0.5 and temp < 0.6
-- SELECT * FROM hour WHERE temp BETWEEN 0.5 and 0.6
-- SELECT * FROM hour WHERE weekday IN (1,2,3,4,5)
-- SELECT * FROM hour WHERE dteday LIKE ('2011%')
-- SELECT * FROM hour WHERE dteday GLOB "2011*"

/*

 sqlite 에서 사용 가능한 정규표현식
 *, ?, []
 
 */


-- 2011 or 2012 로 시작하는 문자열
-- SELECT * FROM day WHERE dteday GLOB "201[12]*" 
-- SELECT * FROM day WHERE dteday GLOB "[0-9]*-[0-9]*-[0-9]*" 
-- SELECT * FROM day WHERE dteday GLOB "[0-9][0-9][0-9][0-9]-[0-9]*-[0-9]*" 

-- 결측치 확인
-- SELECT * FROM hour WHERE casual IS NULL

-- 중복제거
-- SELECT DISTINCT weathersit FROM hour;
-- SELECT ALL weathersit FROM hour;

-- top10 

-- SELECT dteday, cnt FROM day ORDER BY cnt DESC LIMIT 10, 20

-- GROUP BY

-- SELECT season, sum(cnt) FROM hour GROUP BY season
-- SELECT yr, mnth, sum(cnt), avg(temp) FROM hour GROUP BY yr, mnth
-- SELECT workingday, avg(cnt) FROM hour GROUP BY workingday
-- SELECT weathersit, sum(cnt) FROM hour GROUP BY weathersit
-- SELECT hr, sum(cnt) FROM hour GROUP BY hr

-- HAVING

/*
SELECT yr, mnth, sum(cnt), avg(temp) 
FROM hour 
GROUP BY yr, mnth
HAVING avg(temp) > 0.5
*/

/*
SELECT yr, mnth, sum(cnt), avg(temp) 
FROM hour 
GROUP BY yr, mnth
HAVING sum(cnt) > 100000
*/

-- join
/*
	inner join
	outer join 
	left join 
	right join
	
	cross join
	
*/

-- inner join: 두 테이블간의 일치하는 컬럼이 존재하는 경우에만 조회하는 경우

/*
SELECT 
	day.dteday,
	hour.hr
FROM day
INNER JOIN hour 
ON day.dteday = hour.dteday
*/

/*
SELECT 
	day.cnt
	myTable.name
FROM day
INNER JOIN myTable
ON day.instant = myTable.id

*/

/*
SELECT 
	day.cnt,
	myTable.name
FROM day
LEFT OUTER JOIN myTable
ON day.instant = myTable.id
*/

/*
SELECT
	day.cnt,
	myTable.name
FROM myTable
INNER JOIN day
ON myTable.id = day.instant
*/

/*
SELECT
	day.instant,
	day.cnt,
	myTable.id,
	myTable.name
FROM myTable
LEFT OUTER JOIN day
ON myTable.id = day.instant
*/

SELECT
	day.instant,
	day.cnt,
	myTable.id,
	myTable.name
FROM day
CROSS JOIN myTable
```   


