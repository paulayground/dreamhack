# Category

crypto

# Overview

`rot128.py`는 `flag.png` 파일을 암호화하여 `encfile`로 저장하는 프로그램의 소스 코드입니다. (풀이자가 프로그램을 직접 실행할 수는 없습니다.)

주어진 `encfile`을 복호화하여 flag 파일 내용을 알아낸 뒤, `flag.png`에서 플래그를 획득하세요!

플래그의 형식은 `DH{...}` 입니다.

# Analysis

```py
# rot128.py

# 0~255까지의 숫자를 2자리 16진수 리스트로 변환
hex_list = [(hex(i)[2:].zfill(2).upper()) for i in range(256)]

with open('flag.png', 'rb') as f:
    plain_s = f.read()

# flag.png의 바이트를 2자리 16진수 리스트로 변환
plain_list = [hex(i)[2:].zfill(2).upper() for i in plain_s]

enc_list = list(range(len(plain_list)))

# hex_list에 맞춰서 +128 mod 256 연산
for i in range(len(plain_list)):
    hex_b = plain_list[i]
    index = hex_list.index(hex_b)
    enc_list[i] = hex_list[(index + 128) % len(hex_list)]

enc_list = ''.join(enc_list)

with open('encfile', 'w', encoding='utf-8') as f:
    f.write(enc_list)
```

`flag.png`의 바이트를 128을 더해서 변환된 내용을 `encfile`로 저장하는 코드로, 복호화를 위해 `encfile` 바이트에 같은 방식으로 128을 더하게 되면 원본파일인 `flag.png`를 얻을 수 있다.

# Exploitation

`encfile`에서 가져온 바이트를 다시 128을 더해주면서 ROT 128 복호화를 시켜 원본 `flag.png` 파일을 얻을 수 있다.

```py
# solve.py
# encfile 읽기
with open("./encfile", "r", encoding="utf-8") as f:
    enc_s = f.read().strip()

# hex를 바이트 데이터로 변환
enc_bytes = bytes.fromhex(enc_s)

# ROT 128 복호화
plain_bytes = bytes([(b + 128) % 256 for b in enc_bytes])

# 복구된 이미지 저장
with open("flag.png", "wb") as f:
    f.write(plain_bytes)
```

# Flag

`DH{y0...t?}`
