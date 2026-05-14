# encfile 읽기
with open("./encfile", "r", encoding="utf-8") as f:
    enc_s = f.read().strip()

# hex를 바이트 데이터로 변환
enc_bytes = bytes.fromhex(enc_s)

# ROT 128 복호화
plain_bytes = bytes([(b + 128) % 256 for b in enc_bytes])

# 복구된 이미지 저장
with open("flag.png", "wb") as f:
    f.write(plain_bytes)