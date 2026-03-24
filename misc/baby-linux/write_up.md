1. 플라스크로 구성된 웹서버로 post / 요청 시 유저가 작성한 데이터를 실제 커맨드로 실행하는 코드가 존재하며, 실행한 명령의 결과를 리턴하는 코드를 확인함. 
추가로 유저의 요청에 flag가 들어가면 No를 뱉는 flag를 직접 쓰지 말라는 코드도 확인.

2. 접속한 index 화면에서 ls -l로 해당 서버의 디렉토리구성을 확인.
dream이라는 웹서버와 상관이 없어보이는 디렉토리 발견.
ls -l /dream 을 통해 계속 내부로 들어가 flag.txt 파일 발견(cat hint.txt를 통해 flag의 위치도 확인가능)
flag를 요청에 직접 넣으면 No를 리턴하기 때문에 cat dream/hack/hello/fl?g.txt 등 와일드카드 마스크를 통해 flag 확인.
* find . -name "fl?g.txt" 를 통해 flag.txt의 경로를 쉽게 알 수 있는 방법도 있었다.