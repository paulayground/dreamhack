# 배운 점

# 풀이 과정 기록

제시된 `chall` 이진파일을 `ghidra`를 통해 확인하였으며, `FUN_00101288`함수에서 시작되는 프로그램이였다.

써있는 코드를 읽어가면서 어떤 코드의 내용인지 확인했다.

`if (sVar5 == sVar4) {}`를 통해 정답이 적힌 배열인 `d9xJaU5YpMiK9t71WlG`의 길이와 같은 19자리라는 것을 확인하였다.

`FUN_001011a5` 함수를 통해 기준 문자열에서 `(local_c + 3 + local_10) % 0x3e`를 통해 치환된 값이 반환되고 그값이 `d9xJaU5YpMiK9t71WlG`와 일치하는 경우를 묻는 문제였다.

local_c는 각 문자열인덱스로 0,1,2,3... 증가하는 값이며, local_10은 기준문자열에서 찾은 인덱스의 값

`d9xJaU5YpMiK9t71WlG`를 역으로 돌렸을 때 값을 구하기로 결정하고 `(local_c + 3 + local_10)`만큼를 앞으로 돌려 나온 값으로 구하여 해결했다.

```c
// 메인함수
undefined8 FUN_00101288(void){
  int iVar1;
  char *pcVar2;
  undefined8 uVar3;
  size_t sVar4;
  size_t sVar5;
  char local_348 [256];
  // 정답이 들어있는 배열
  char local_248 [32];
  // 빈 배열
  char local_228 [256];
  // 사용자 입력값
  char local_128 [256];
  FILE *local_28;
  int local_1c;

  setvbuf(stdin,(char *)0x0,2,0);
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stderr,(char *)0x0,2,0);
  // local_248에 d9xJaU5YpMiK9t71WlG 입력
  builtin_strncpy(local_248,"d9xJaU5YpMiK9t71WlG",0x14);

  printf("Enter the secret key: ");
  // 사용자의 stdin를 local_128에 넣음
  pcVar2 = fgets(local_128,0x100,stdin);

  // 입력 에러 처리
  if (pcVar2 == (char *)0x0) {
    puts("Input error!");
    uVar3 = 1;
  } else {
    sVar4 = strlen(local_128);
    local_1c = (int)sVar4;
    if ((0 < local_1c) && (local_128[local_1c + -1] == '\n')) {
      local_128[local_1c + -1] = '\0';
      local_1c = local_1c + -1;
    }

    sVar5 = (size_t)local_1c;
    sVar4 = strlen(local_248);

    // 사용자 입력값과 정답배열의 입력값 길이 확인
    if (sVar5 == sVar4) {
      FUN_001011a5(local_128,local_228,local_1c);
      iVar1 = strcmp(local_228,local_248);
      if (iVar1 == 0) {
        puts("Correct! Here is your flag:");
        local_28 = fopen("flag","r");
        if (local_28 == (FILE *)0x0) {
          puts("Flag file not found!");
        } else {
          pcVar2 = fgets(local_348,0x100,local_28);
          if (pcVar2 != (char *)0x0) {
            printf("%s",local_348);
          }
          fclose(local_28);
        }
      }
      else {
        puts("Wrong key!");
      }
      uVar3 = 0;
    }
    else {
      puts("Wrong key length!");
      uVar3 = 1;
    }
  }
  return uVar3;
}

/**
 * 사용자의 입력값을 계산을 통해 순서 변경
 * @param 사용자 입력값, 빈배열, 사용자 입력값 길이(19)
 **/
void FUN_001011a5(long param_1,long param_2,int param_3){
  int local_14;
  int local_10;
  int local_c;

  local_c = 0;

  do {
    if (param_3 <= local_c) {
      *(undefined1 *)(param_2 + param_3) = 0;
      return;
    }

    local_10 = -1;
    // 0x3e = 62
    // 반복하면서 입력값의 자리수와 기준문자열을 하나씩 꺼내서 비교하여 해당 위치의 값을 local_10에 할당
    for (local_14 = 0; local_14 < 0x3e; local_14 = local_14 + 1) {
      if (*(char *)(param_1 + local_c) ==
          "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM"[local_14]) {
        local_10 = local_14;
        break;
      }
    }

    if (local_10 == -1) {
      *(char *)(local_c + param_2) = *(char *)(param_1 + local_c);
    } else {
      // 기준 문자열에서 local_c + 3 + local_10을 통해 치환된 값을 가져옴
      *(char *)(local_c + param_2) =
           "qwertyuiopasdfghjklzxcvbnm0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
           [(local_c + 3 + local_10) % 0x3e];
    }
    local_c = local_c + 1;
  } while( true );
}
```

# 익스플로잇 코드 정리

solve.py

# 심화 학습 (Deep Dive)

# 참고
