l = ["p","y","t","h","o","n"]
print("".join(l))


# 두 개 뽑아서 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/68644?language=python3

numbers=[2,1,3,4,1]

answer = []
n = len(numbers)
    
for i in range(n-1) :
    for j in range(1,n) :
        if i != j :
            sum = numbers[i] + numbers[j]
            
        if sum not in answer :
            answer.append(sum)
answer. sort()

print(answer)

# 특이한 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/120880?language=python3

numlist =[1,2,3,4,5,6]
n = 4

answer = []
k = len(numlist)

    
for i in range(k) :
    for j in range(i+1, k) :
        if abs(n - numlist[i]) > abs(n - numlist[j]) :
            numlist[i], numlist[j] = numlist[j], numlist[i]
        elif abs(n - numlist[i]) == abs(n - numlist[j]) and numlist[i] < numlist[j]:
            numlist[i], numlist[j] = numlist[j], numlist[i]

print(numlist)

print(1 if 1>0 else 0)
print('abc' if 1>0 else 'bcd')

if 1>0 :
    print('abc')
else :
    print('bcd')


# 하샤드 수
# https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3

x = 12

k = [int(k) for k in str(x)]
print(k)
s = 0

for i in range(len(k)) :
    s = s + int(k[i])
        
if x % s == 0 :
    print('true')

# 문자열 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12917?language=python3

s='Zbcdefg'

answer = ''
list_s = list(s)
n = len(list_s) 

# list_s = list(s)
# list_s.sort()
# list_s.reverse()

for i in range(0, n-1) :
    for j in range(i+1, n) :
        if list_s[i] < list_s[j] :
            list_s[i], list_s[j] = list_s[j], list_s[i]
            
answer = "".join(list_s)
print(answer)

# 추억 점수
# https://school.programmers.co.kr/learn/courses/30/lessons/176963

answer = []
name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
sum = 0

print(photo[0])
print(name[0])
print('yes' if name[0] in photo[0] else 'no')

for i in range(len(photo)) :
    for j in range (len(name)) :
        if name[j] in photo[i] :
            sum += int(yearning[j])
    answer.append(sum)
    sum = 0

# for pt in photo :
#         sum_score = 0
#         for j in pt :
#             if j in dict_p :
#                 sum_score += dict_p[j]
#         answer.append(sum_score)

print(answer)

# 크기가 작은 부분 문자열
# https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=python3

# 문자열 길이 n
# 부분 문자열 길이 k

# k -> 1, n개의 문자가 생김
# k -> 2, n-1 개의 문자
# k -> 3, n-2 개의 문자

answer = 0

t = '3141592'
p = '271'

n = len(t)
k = len(p)

for i in range(n-k+1) :
    if t[i:i+k] <= p :
        answer += 1

print(answer)




