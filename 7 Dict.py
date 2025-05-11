#dict
a = {}
print(type(a))

# set
b = {1}
print(type(b))

c = dict()
c = {1: 'a', 'b' : 'b'}
print(c)

# 인덱스 X 키O
c[2] = 'c'
c['c'] = 2
print(c)

del(c[2])
del(c['b'])
print(c)

print(c.get(2))

# 키는 유일 중복X, 값은 중복 가능
print('c' in c) # print('c' in c.key())
print(2 in c.values())

dic = {
    "비트": "0이나 1의 값을 가지는 컴퓨터 데이터의 최소 단위",
    "변수": "어떤 1개의 자료를 저장하기 위한 메모리 할당 공간",
    "리스트": "여러 개의 연속적인 자료를 저장하는 자료구조"
}


print("★ 컴퓨터 사전 ★")
word = input("검색할 단어를 입력하세요: ")
if word in dic :
    print(f'{word}: {dic[word]}')
else :
    print("정의된 단어가 없습니다.")

# 실습 1(백준 문제) - 정답
n, m= map(int, input().split())

set_n = set()
num = 0

for i in range(n) :
    set_n.add(input())

for j in range(m) :
    t = input()
    if t in set_n :
        num += 1

print(num)

# 학생 딕셔너리 생성 및 데이터 추가
student = {'Alice' : 85, 'Bob' : 90, 'Charlie' : 95}
print(student)

# 학생 추가
student['David'] = 80
print(student)

# 학생 점수 수정
student['Alice'] = 88
print(student)

# 학생 삭제
del(student['Bob'])
print(student)

# 학생 전체 출력
for s in student.keys() :
    print(s, student[s])
    # print(f'{s} : {student[s]}')
    # print(f'{s} : {student.get(s)})