# 기준 문자열
template = "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM"

# 치환된 이후의 값
after = "d9xJaU5YpMiK9t71WlG"

# 치환되기 전의 값
before = ""

for i in range(len(after)):
    idx = template.find(after[i])
    # (local_c + 3 + local_10) % 0x3e를 역으로 계산
    before += template[(idx - i - 3) % 62]

print(before)
