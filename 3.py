song = input("너의 최애 노래는? ")
print(song)
print(type(song))

a = input("1+1=? ")
print(a)
print(type(a)) # a는 str
# print(a+2) 문자 2 + 숫자 2 => 연산 불가 
print(a*2) #문자열 취급 => 문자 2번
print(int(a)+2) # 숫자 2 + 2

# num = int(input()) 출력값 정수형 변경
# ff = float(input()) 출력값 실수형 변경

a = 2
print(str(a)*10)
print(str(a)+"입니다")
# print (2+"입니다") 에러

# 실습 2
print("|\\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"\'    |")
print("||_/=\\\\__|")

print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"\'    |')
print('||_/=\\\\__|')

print('|\_/|') # ''이든 ""이든 \ 쓸 때 하나는 문자로 인식함
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"\'    |')
print('||_/=\\\\__|')


# 최종 결과
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print('|"^"`    |')
print("||_/=\\\__|")

# 실습 3
name = input("이름을 입력하세요. ")
age = input("나이를 입력하세요. ")
print(f"안녕하세요! {name}님 ({age}세) \n")


name = input("이름을 입력하세요. ")
birth_year = int(input("태어난 년도를 입력하세요. "))
now_year = int(input("올해 년도를 입력하세요. "))
print(f"올해는 {now_year}년, {name}님의 나이는 {now_year-birth_year}세 입니다.")