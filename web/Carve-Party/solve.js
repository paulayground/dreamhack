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

// 변경된 pumpkin배열의 값을 ASCII 문자열로 반환
const flag = pumpkin.map((x) => String.fromCharCode(x)).join("");
console.log(flag);