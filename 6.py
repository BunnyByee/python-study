print("오늘은 12월 %d일 입니다." % 2)
print("오늘은 %d월 %d일 입니다." %(12,2))
print("오늘은 %d%s %d일 입니다." %(12,'월',2))
print(f"오늘은 {12}{'월'} {2}일 입니다.") # 깔끔
print("오늘은 "+str(12)+"월 "+str(2)+"일 입니다.")
print("오늘은 ",12,"월 ",2,"일 입니다.") # 깔끔

print("Hello".upper()) # 대문자
print("Hello".lower()) # 소문자

friends = "고찬국 김다운 김민창"
a = friends.split() # 디폴트는 띄어쓰기 " "
print(a)