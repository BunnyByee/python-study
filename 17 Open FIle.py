with open('./output/data.bin','wb') as f:
    txt = '안녕'
    f.write(txt.encode()) # 암호화

with open('./output/data.bin','rb') as f:
    data = f.read()
    print(data)
    print(data.decode()) # 복호화

with open('./output/mymelody.jpg', 'rb') as f:
    img = f.read()

# img로 읽어서 다른 파일에 같은 이미지로 변경하기
with open('./output/mymelody2.jpg', 'wb') as f:
    f.write(img)
