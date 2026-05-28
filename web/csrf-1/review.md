# `<img src=/admin/notice_flag?userid=admin>, <object data=/admin/notice_flag?userid=admin>`

브라우저가 HTML 파싱중에 img 태그의 경우 바로 요청시도하는데 object의 경우 임베디드된 페이지를 만들기 때문에 그 시간 사이에 셀레니움봇의 quit()가 먼저 발생할 수 있다.

# `<meta http-equiv="refresh" content="5; url=http://이동할주소">`

새로고침이 가능함
