# # 실습 4
# import sys
# input = sys.stdin.readline

# # 아래 코드만 있으면 시간 초과, ↑ 위 코드 필요!
# n = int(input())
# stack = []

# # 함수
# def push_s(x) :
#     stack.append(x)

# def pop_s() :
#     if len(stack) == 0 :
#         print(-1)
#     else :
#         print(stack.pop())

# def size_s() :
#     print(len(stack))

# def empty_s() :
#     if len(stack) == 0 :
#         print(1)
#     else :
#         print(0)

# def top_s() :
#     if len(stack) == 0 :
#         print(-1)
#     else :
#         print(stack[-1])

# # 본 프로그램 
# for i in range(n) :
#     command = input().split() # 리스트 처리, # 리스트 첫번째 값 = 명령 텍스트, 두번째 값 = 정수
#     if len(command) == 2 : # 리스트 개수가 2개면 push 입력
#         push_s(command[1])
#     elif command[0] == 'pop' :
#         pop_s()
#     elif command[0] == 'size' :
#         size_s()
#     elif command[0] == 'empty' :
#         empty_s()
#     elif command[0] == 'top' :
#         top_s()

# # match - case 문
#     match command :
#         case ['push', z] :
#             push_s(z)
#         case ['pop'] :
#             pop_s()
#         case ['size'] :
#             size_s()
#         case ['empty'] :
#             empty_s()
#         case ['top'] :
#             top_s()

# 실습 5
def get_times(x) :
    global count
    
    for i in range(1,31) :
        if i % x == 0 :
            count += 1
            print(i, end=' ')

count = 0
n = 3
get_times(n)
print(f'\n{n}의 배수의 개수: {count}')