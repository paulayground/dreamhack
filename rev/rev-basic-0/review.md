# 배운 점

# 풀이 과정 기록

윈도우에서 생성된 `x86` 이진파일이며, `ida`를 통해 리버싱을 진행했다.

메인 함수에서 사용자의 입력값을 받아서 `sub_140001000` 함수를 통해 `if`문이 시작된다.

`sub_140001000` 함수에서는 지정된 문자열 `Compar3_the_str1ng`와 일치하는지 판단하는 함수이다.

```c
int __fastcall main(int argc, const char **argv, const char **envp){
  char v4[256]; // [rsp+20h] [rbp-118h] BYREF

  memset(v4, 0, sizeof(v4));
  sub_140001190("Input : ", argv, envp);
  sub_1400011F0("%256s", v4);
  if ( (unsigned int)sub_140001000(v4) )
    puts("Correct");
  else
    puts("Wrong");
  return 0;
}

_BOOL8 __fastcall sub_140001000(const char *a1){
  return strcmp(a1, "Compar3_the_str1ng") == 0;
}
```

코드 내에 지정되어 있는 `Compar3_the_str1ng`을 입력하게되면 `Correct`가 출력되며, flag 형식에 맞게 `DH{}`를 감싸주면 된다.

# 익스플로잇 코드 정리

# 심화 학습 (Deep Dive)

# 참고
