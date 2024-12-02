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

sentence = '오늘은 {}월 {}일 입니다.'.format(12,2); print(sentence)
sentence = '오늘은 {0}월 {1}일 입니다.'.format(12,2); print(sentence)
sentence = '오늘은 {1}월 {0}일 입니다.'.format(12,2); print(sentence)

b = "   111   222   "
print(b.strip())
print(b.split())
print(b.replace("222","111"))

# 실습 2
num1 = int(input("첫 번째 자연수 : "))
num2 = input("두 번째 자연수 : ")

f = (num1*int(num2[2])); print(f) # 일의 자리 계산
s = (num1*int(num2[1])); print(s) # 십의 자리 계산
t = (num1*int(num2[0])); print(t) # 백의 자리 계산

result = f+s*10+t*100; print(result) # 총 합계 계산
# result = num1 * int(num2) # 곱하면 결과값이 바로 나오잖아..