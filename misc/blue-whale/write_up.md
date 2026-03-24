[dive 이용]
1. dockerfile에 빌드과정 중 flag를 /home/$user/flag로 옮긴 뒤 flag의 내용을 읽어 파일로 생성하는 코드를 확인
2. dive를 통해 해당 blue-whale 이미지를 분석해 삭제하기 전의 레이어의 파일 구조 상태를 확인하여 flag 획득

---
[dive 미이용]
1. dockerfile에 빌드과정 중 flag를 /home/$user/flag로 옮긴 뒤 flag의 내용을 읽어 파일로 생성하는 코드를 확인
2. flag가 삭제가 되는 코드가 있더라도 도커의 레이어는 레이어별로 저장되기 때문에 삭제되기 전의 코드가 레이어에 남아있다.
3. `docker save <IMAGE> -o <NAME>.tar` 로 도커의 이미지를 tar로 파일로 저장해 내용을 보게되면 `menifest.json` 에 `Layers` 배열의 레이어들을 확인할 수 있다.
4. 해당 레이어를 확인하여 마지막에 flag가 생성되었던 위치인 `/home/chall`를 확인해보면 flag를 찾을 수 있다.
* 쉘스크립트를 통해 blobs안에 있는 tar 레이어들의 flag값이 매칭되는 것을 가져올 수 있다.
* 해당 파일을 `file`을 통해 확인해보면 `POSIX tar archive` 로 확인되는 것을 볼 수 있다.
* rm * 이후의 레이어에서는 제거된 파일들에 대해 whiteout 파일이 생성되어 .wh. 같이 마킹이 되지만, 이전 레이어에는 실제 파일이 그대로 남아있다.
```bash
for f in blobs/sha256/*; do
  if file "$f" | grep -q tar; then
    echo "===== $f ====="
    tar -tf $f | grep home/chall/
  fi
done

===== blobs/sha256/1ec8100a12f42403151c8f0dfef2ae5505d43f6a1364958b1ef498fa74efa088 =====
home/chall/
home/chall/flag
===== blobs/sha256/2338e6ed1a632e22640fd2fcb9049738ad32eb4104ef43865a31107084791d88 =====
home/chall/
home/chall/DH{FLAG}
===== blobs/sha256/34cc74a5e40511ff1596847d7da934c703dd93906f11df9c205c3143decedbee =====
===== blobs/sha256/3747ca90832a757949a3fcf1ecf2798024fbd1869155332803583ab61e04c689 =====
home/chall/
home/chall/.bash_logout
home/chall/.bashrc
home/chall/.profile
home/chall/flag
===== blobs/sha256/60dad543d375aaea270582227e1fa8a8b9f91a6c9f21bd2b9a4175b62b21754a =====
home/chall/
home/chall/.bash_logout
home/chall/.bashrc
home/chall/.profile
===== blobs/sha256/6515074984c6f8bb1b8a9962c8fb5f310fc85e70b04c88442a3939c026dbfad3 =====
===== blobs/sha256/89f8564b4d2f3ecb97b19051ece7fa44d9304f4bc787ac5acfd6cfbe420d663d =====
home/chall/
home/chall/.wh.DH{FLAG}
home/chall/.wh.flag
===== blobs/sha256/ed43cbe2a365c3ac25a85d4919f4d07b1522055b663b6a49cdffa36304b2c33b =====
```
