# Category

web

# Overview

개발자 도구의 Sources 탭 기능을 활용해 플래그를 찾아보세요.

플래그 형식은 DH{...} 입니다.

# Analysis

- 제시된 소스의 `main.4c6e144e.map`파일로도 소스맵 파일이 존재하는 것을 알 수 있지만, 개발자도구 `source` 탭에서 `webpack://`을 통해 소스맵 파일이 존재한다는 것을 확인할 수 있으며, `webpack://`내에 번들링 되기 전 원본 css 파일의 이름인 `main.scss`파일이 존재하는 것을 알 수 있다.
- `main.4c6e144e.map`파일을 살펴보면 원라인으로 펼쳐져있지만 map파일은 `json`구조를 가지고 있어 정렬하면 아래와 같은 구조를 가지며, json 내부의 `file`을 통해 map파일이 `main.3da94fde.css`파일과 매핑되는 것을 알 수 있다.
  ```json
  {
    "version": 3,
    "file": "main.3da94fde.css",
    "sources": ["webpack:///./styles/main.scss"],
    "sourcesContent": [
      "@import url ... // WEBPACK FOOTER //\n// ./styles/main.scss"
    ],
    "mappings": ",yKAEA;;;;AAIA;AACA;AACA;AAiLA",
    "sourceRoot": ""
  }
  ```
  map파일 배포로 인한 원본코드 노출로 해당 원본 코드에서 flag의 존재가능성을 확인할 수 있다.

# Exploitation

`webpack://`의 `main.scss` 파일 하단을 통해 번들링되며 사라졌었던 flag가 작성된 주석을 확인할 수 있다.
또는 개발자도구 `search` 탭을 이용해서 flag시작 단어인 `DH`를 검색하여 찾을 수 있다.

# Flag

`DH{2e...d5}`
