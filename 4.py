a = []
b = [1, 2, 3, 4]
c = ["장원영", "안유진"]
d = [1, "아이브"]

# print(len(c))
# print(c[0])
# print(c[1])

# c[0] = "카리나" # 리스트 항목 변경
# print(c)

# del c[0] # 리스트 항목 삭제
# print(c)

# c.append("윈터") # 리스트 항목 추가
# print(c)

print(b[-1]) #음수는 역순으로 
print(b[-2])
print(type(b))

seasons = ["봄", "여름", "가을", "겨울"]
print(seasons[0:1]) # 시작점부터 1 앞까지 
print(seasons[0:2]) # 시작점부터 2 앞까지
print(seasons[:2]) # 처음부터 2 앞까지
print(seasons[1:]) # 1부터 끝까지
print(seasons[1:3]) # 1부터 3 앞까지
print(seasons[:]) #처음부터 끝까지 print(seasons)
print(seasons[::3]) #처음부터 끝까지, 간격 3
print(seasons[::-1]) # 뒤집어서 출력

seasons2 = ["봄", "여름", "가을", "겨울",[1,2,3,4]]
print(seasons2[-1]) # 리스트 하나 통째로
print(seasons2[-1][0]) #리스트 2의 0번

# 리스트 더하기 + => 리스트 합치기
# 리스트 곱하기 * => 리스트 반복 출력