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