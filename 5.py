a = [3,4,2,1]
a.sort()
# a.sort(reverse=True)
a.reverse() # a[::-1]
print(a)

b=["a","d","c","b"]
b.sort()
print(b)

c=["1","10","11","2"]
c.sort()
print(c)

d=["강북", "강남", "서","ffdfd", "서", "서"]

print(d)

print(d.index("서"))
first = d.index("서")+1
print(first + d[first:].index("서"))
d.count("서") # 개수 세기

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
# 1. 2번 인덱스값 출력
print(rainbow[2])
# 2. 알파벳 순서로 정렬한 값 출력
rainbow.sort()
print(rainbow)
# 3. 좋아하는 색 맨 마지막에 추가하기
rainbow.append("pink")
print(rainbow)
# 4. 3~6번째 값 삭제하기
del rainbow[3:7]
print(rainbow)

rainbow.insert(3,"가") # 특정 인덱스 위치에 요소 추가
print(rainbow)
rainbow.pop(0) # 특정 인덱스 위치에서 요소 삭제
print(rainbow)
rainbow.pop() # 맨 마지막 요소 삭제
print(rainbow)