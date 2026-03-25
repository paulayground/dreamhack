# 배운 점

`.map` 파일: 소스맵파일로 디버그용도로 사용되며, 웹팩 번들링을 통해 난독화나 용량등이 줄어진 js나 css와 연결시켜주는 파일. map파일을 서버에 노출하면 원본 코드가 배포한 것과 같기 때문에 제외하고 배포해야한다.
`json`형태로 이루어져있으며, `file`에 어떤 파일과 매핑이되는지 확인할 수 있으며, `sourcesContent`에는 해당 원본 소스가 나와있다.

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

# 풀이 과정 기록

# 익스플로잇 코드 정리

# 심화 학습 (Deep Dive)

map 파일이 노출되지 않게 prod, dev의 분기 등의 조치를 취해야한다.

# 참고
