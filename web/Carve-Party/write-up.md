# Category

web

# Overview

할로윈 파티를 기념하기 위해 호박을 준비했습니다! 호박을 10000번 클릭하고 플래그를 획득하세요!

# Analysis

클릭할때마다, 조건식에 따라 총 100번 `pumpkin`배열에 `pie`값이 XOR되며 연산할때마다 `pie`값이 변경된다.

```js
var pumpkin = [
  124, 112, 59, 73, 167, 100, 105, 75, 59, 23, 16, 181, 165, 104, 43, 49, 118,
  71, 112, 169, 43, 53,
];
var pie = 1;

// ...

if (counter <= 10000 && counter % 100 == 0) {
  for (var i = 0; i < pumpkin.length; i++) {
    pumpkin[i] ^= pie;
    pie = ((pie ^ 0xff) + i * 10) & 0xff;
  }
}
```

10000번을 넘게 클릭할 경우 해당 조건문 내용이 실행되며, `txt` 변수가 `canvas` 태그에 그려지게 된다.

문제의 제시된 내용처럼 10000번 이상의 클릭을 했을 때의 실행코드이며, 그 외 특이한 내용이 없는 것으로 보아 `txt` 변수가 flag임을 유추할 수 있다.

```js
if (10000 < counter) {
  // ...
  var ctx = document.querySelector("canvas").getContext("2d");
  txt = pumpkin.map((x) => String.fromCharCode(x)).join("");
  // ...
}
```

# Exploitation

`txt`결과만 가져오기 위해 소스코드에서 필요한 부분만 가져오며, XOR연산이 되는 부분의 조건은 `counter <= 10000 && counter % 100 == 0`로 10000번 이상 클릭할 때까지 총 100번 일어나기 때문에 100번 반복한다.

```js
// solve.js
const pumpkin = [
  124, 112, 59, 73, 167, 100, 105, 75, 59, 23, 16, 181, 165, 104, 43, 49, 118,
  71, 112, 169, 43, 53,
];
let pie = 1;

// 100번 반복
for (let _ = 0; _ < 100; _++) {
  // pumpkin 배열 XOR연산 부분
  for (let i = 0; i < pumpkin.length; i++) {
    pumpkin[i] ^= pie;
    pie = ((pie ^ 0xff) + i * 10) & 0xff;
  }
}

// 변경된 pumpkin배열의 값을 유니코드 문자열로 반환
const flag = pumpkin.map((x) => String.fromCharCode(x)).join("");
console.log(flag);
```

# Flag

`DH{I_...i3}`
