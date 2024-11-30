# print("hello world !") ctrl + / >> 자동 한줄 주석처리
print("hello","Python",1 ,2, "asdrf", sep=" a ") # sep=""
print()
print("1")
print("안녕하세요 ", end="")
print("코딩온입니다.")

ive = "I AM"
print(ive)
ive ="장원영"
print(ive)

print(f"나는 {ive}입니다.")
print("나는 ",ive,"입니다.",sep="")
print("나는 "+ive+"입니다.")

# 하 커밋 연습중입니다아.
# 아니 이게 업로드가 안되는 이유가 readme.md 파일 때문이었다!

print(type(77))
print(type(7.2))
print(type("ive"))
print(type('ive')) # 둘다 문자열로 인식 '', ""

# 파이썬의 기능 같은 변수명을 사용할수 있음. 내부적으로는 다름.
a=77
print(type(a))
a=7.2
print(type(a))
a="ive"
print(type(a))

print("What\'s your name?")