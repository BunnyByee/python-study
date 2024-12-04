# 실습 5
numbers = input("숫자 여러 개 입력 > ").split()
numbers = [int (n) for n in numbers]
print(numbers)

max_n = max(numbers)
min_n = min(numbers)

print(f"가장 큰 값: {max_n}")
print(f"가장 큰 값: {min_n}")

hap = 0
for i in numbers :
    hap += i
hap = hap - (max_n + min_n)
count = len(numbers) - 2

print(f"나머지 값의 평균 = {hap/count}")

t1 = (10,20,30)
print(type(t1))
print(t1)
print(t1[0])
# del t1[0] 튜플 요소 삭제X.
# t1[0] = 3 튜플 요소 변경X.
del t1

t2 = (10)
t3 = (10,)
t4 = 10, 20
print(type(t4))

# set 중복된 문자는 한번만 저장 => 중복X 라고 하면 set 사용하면 됨.
set1 = {1,2,3,3}
print(set1)
set2 = set([1,2,3,3,4])
print(set2)
set2.add(5)
print(set2)

while len(set2) > 0 :
    a = set2.pop() # 랜덤
    print(a)

l1 = [1,2,3,4]
while len(l1) > 0 :
    a = l1.pop() # 마지막 것이 나옴.
    print(a)

set3 = set('apple')
print(set3)
while len(set3) > 0 :
    a = set3.pop()
    print(a)

name = ['1','2','3','2']
a = []

for i in range(0, len(name)):
    if a.count(name[i]) < 1 :
        a.append(name[i])
print(a)

# 중복값 구하기
for i in range(len(name)):
    if name.count(name[i]) > 1 :
        print(name[i])



name_set = set(name)
print(name_set)
name_list = list(name_set)
name_list.sort()
print(name_list)
