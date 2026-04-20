# Category

rev

# Overview

이 문제는 사용자에게 문자열 입력을 받아 정해진 방법으로 입력값을 검증하여 `correct` 또는 `wrong`을 출력하는 프로그램이 주어집니다.

해당 바이너리를 분석하여 `correct`를 출력하는 입력값을 찾으세요!

획득한 입력값은 `DH{}` 포맷에 넣어서 인증해주세요.

예시) 입력 값이 `Apple_Banana`일 경우 flag는 `DH{Apple_Banana}`

# Analysis

윈도우에서 생성된 `x86` 이진파일이며, `ida`를 통해 리버싱을 진행했다.

메인 함수에서 사용자의 입력값을 받아서 `sub_140001000` 함수의 결과로 시작되는 `if`문이 존재한다.

`sub_140001000` 함수에서는 사용자가 입력한 문자열과 `Compar3_the_str1ng`와 일치하는지 판단하는 함수이다.

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

# Exploitation

if문을 통과하기 위해 입력값으로 `Compar3_the_str1ng`을 입력하면 `Correct`가 출력되며, `Compar3_the_str1ng`를 flag 형식에 맞게 `DH{}`를 감싸주면 된다.

# Flag

`DH{Co...ng}`
