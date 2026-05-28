# Category

web

# Overview

여러 기능과 입력받은 URL을 확인하는 봇이 구현된 서비스입니다.

CSRF 취약점을 이용해 플래그를 획득하세요.

# Analysis

- POST `/flag`에서는 `session_id`를 생성한 뒤, 세션에 `admin` 문자열을 저장한다.

  이후 사용자가 입력한 `param`과 함께 다음 형태의 쿠키를 `check_csrf()`에 전달한다.

  ```py
  {"name":"sessionid", "value": session_id}
  ```

  `check_csrf()`는 다음 url을 생성하고, url과 쿠키를 `read_url()`로 전달한다.

  ```
  http://127.0.0.1:8000/vuln?param=<USER_INPUT>
  ```

  `read_url()`에서 셀레니움 봇은 쿠키를 포함하여 url에 접속한다.

- GET `/vuln`에서는 `param`값을 검증하는 `frame`, `script`, `on` 문자열이 `*`로 치환되는`xss_filter`가 존재하며, `body` 태그 내부에 그대로 렌더링한다.

- GET `/change_password`는 쿠키의 `session_id`를 통해 세션에서 `username`을 가져온 뒤, 사용자의 비밀번호를 `pw` 파라미터로 변경한다.

- POST `/login`은 `username`, `password`를 통해 `users` 여부를 판단하고, 일치하면 `session_id`를 세션에 저장하고 쿠키를 생성해 응답한다.

# Exploitation

1. POST `/flag`에서 `param`을 다음과 같이 입력하고 요청한다.

   ```html
   <img src="/change_password?pw=1234" />
   ```

   `img` 태그는 `script`, `on`, `frame`을 사용하지 않기 때문에 `xss_filter` 필터에 적용되지 않는다.

2. 셀레니움 봇은 다음 주소에 접속한다.

   ```
   http://127.0.0.1:8000/vuln?param=<img src="/change_password?pw=1234" />
   ```

3. `/vuln`에서는 `param`이 `body` 내부에 그대로 렌더링되므로 브라우저가 `img` 태그를 생성한다.

4. 브라우저는 이미지 로딩을 위해 자동으로 다음 요청을 전송한다.

   ```
   GET /change_password?pw=1234
   ```

5. `/change_password`에서는 셀레니움 봇이 갖고 있는 쿠키에서 `session_id`를 가져와 `admin`의 `value`를 `1234`로 변경한다.

6. POST `/login`를 통해 `admin`, `1234`로 로그인할 경우 flag를 획득할 수 있다.

# Flag

`DH{c5...ef}`
