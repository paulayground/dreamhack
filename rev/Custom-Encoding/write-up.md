# Category

rev

# Overview

Another Encoding?

# Analysis

제시된 `chall` 이진파일을 `ghidra`를 통해 확인하면, `FUN_00101288` 함수가 메인함수로 시작되는 프로그램인 것을 알 수있다.

코드 분석 결과, 사용자의 입력값과 `d9xJaU5YpMiK9t71WlG`라는 정답이 적힌 `local_248`변수가 일치하면 flag를 획득할 수 있다.

메인 함수 내에서 호출되는 `FUN_001011a5` 함수를 통해 사용자의 입력값이 `qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM`와 같이 제시된 문자열에서 `(local_c + 3 + local_10) % 0x3e`를 통해 치환된 값이 반환되고 그 값이 `d9xJaU5YpMiK9t71WlG`와 같아야한다.
`local_c`는 사용자의 입력값의 각 인덱스로 `0,1,2,3...`과 같이 점차 증가하는 값이며, `local_10`은 제시된 문자열에서 찾은 인덱스의 값이다.

# Exploitation

정답인 `d9xJaU5YpMiK9t71WlG`를 역으로 치환하였을 때 값을 구하기 위해 `(local_c + 3 + local_10)`만큼 반대로 계산하여 앞으로 돌려 나온 값을 얻을 수 있다.

프로그램 실행 후 얻어진 값을 입력하면 flag를 얻을 수 있다.

```py
# solve.py
# 제시된 문자열 틀
template = "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM"

# 치환된 이후의 값
after = "d9xJaU5YpMiK9t71WlG"

# 치환되기 전의 값
before = ""

for i in range(len(after)):
    idx = template.find(after[i])
    # (local_c + 3 + local_10)를 역으로 계산
    before += template[(idx - i - 3) % 62]

print(before)
```

```sh
$ Enter the secret key: p5hAr8v5NFXRxGjplN3
Correct! Here is your flag:
DH{48...79}
```

# Flag

`DH{48...79}`
