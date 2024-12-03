# i = 0
# while i<5 :
#     i+=1
#     print(i)
# print("끝")

# # 무한루프 실행 시 종료하는 법은 ctrl + c

# # 1-10까지 홀수만 출력
# n = 0
# while n < 10 :
#     n += 1
#     if n % 2 != 0 :
#         print(n)

# i = 1
# while i <10 :
#     print(i)
#     i+=2
# # 이 코드가 더 효율적임!

# 실습 1
# sum = 0
# sum_odd = 0

# n = int(input("어디까지 계산할까요? "))
# for i in range (1,n+1) :
#     sum += i
#     if i % 2 != 0 :
#         sum_odd += i
# print(sum)
# print(sum_odd)

# # 실습 2
# n = int(input("몇 초?: "))
# for i in range (n,0,-1) :
#     print(i, end=" ")
# print("발사!!")

# # while의 관점에서도 한 번 생각해보기

# # 실습 3
# dan = int(input("몇 단을 출력할까요? "))

# for i in range(1,10) :
#     print(f"{dan} * {i} = {dan*i}")

# a = [1,2,3,4,5]
# a2 = []
# a3 = []
# a4 = []

# a3 = [i * 3 for i in a]
# print(a3)

# a4 = [i*3 for i in a if i%2 == 0]
# print(a4)

# for y in range(3) :
#     for x in range(2) :
#         print (f"y: {y}, x: {x}")
#     print()

# # 구구단 전체
# for i in range(2,10) :
#     print(f'{i} 단')
#     for j in range(1, 10):
#         print(f'{i} x {j} = {i*j}')
#     print()

# # 좌석 배치도 (행)
# print('*** 자리 배치도 ***')
# customer = int(input('고객 수 입력: '))
# row = int(input('좌석행 수 입력: '))

# if customer % row == 0 :# 나머지 X 면
#     column = customer // row  # 몫으로 열을 나누면 됨 ex) 
# else :
#     column = (customer // row) + 1 # 아니면 몫+1 더 추가

# for i in range(0, row) : # 행 먼저
#     for j in range(1, column +1) : # 행에 맞춰 열에 사람 세우기
#         seat = i * column + j
#         if seat > customer :
#             break
#         print(seat, end= ' ')
#     print()

# 실습 4-1
n = int(input('몇 줄? > '))

for i in range(1,n+1) :
    print("*" * i)

# for i in range(n) : # 0부터 n 미만까지, n번
    # for j in range (i+1): # 1부터 n+1까지, n번
    #     print('*',end='')
    # print()

# 실습 4-2
n = int(input('몇 줄? > '))

for i in range(1,n+1) : # 1부터 n+1까지 , n번
    print(' ' * (n-i) + '*' * i )

# for i in range(1,n+1) : # 1부터 n+1까지 , n번
#     for j in range (n-i): # n-1, n-2, ... , n-n = 0개
#         print(' ',end='')
#     for k in range (i): # 1, 2, 3, ... , n개
#         print('*',end='')
#     print()

# 실습 4-3
n = int(input('몇 줄? > '))

for i in range(1,n+1) : # 1부터 n+1까지 , n번
    print(' ' * (n-i) + '*' * i, end='' )
    print('*' * (i-1))
    # print('*' * (i-1) + ' ' * (n-i) )