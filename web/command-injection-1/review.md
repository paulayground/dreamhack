# 배운 점

# 풀이 과정 기록

`post` `ping`에서 host이름을 수정해가지고 sh로 실행하는구조를 파악했다.
flag경로가 dockerfile 보니까 `/app`에 flag.py로 확인했다.
`8.8.8.8; cat /app/flag.py` 진행했는데 프론트에 정규식이 `[A-Za-z0-9.]{5,20}`걸려있어 해제하고 다시 진행한 결과 `"`매칭 에러로 다시 수정하여
`8.8.8.8"; cat /app/flag.py"` 전송하였고 flag를 획득했다.

# 익스플로잇 코드 정리

solve.py

# 심화 학습 (Deep Dive)

# 참고
