import sys

print(sys.argv)

argv = sys.argv[1:]
print(argv)

print(int(sys.argv[1])+int(sys.argv[2]))


# 과제 1
argv = sys.argv[1:]
sum = 0

for i in argv :
    sum += int(i)

print(sum)


# 과제 2
argv = sys.argv[1:]
result = 0

if len(argv) <= 2 or len(argv) >= 4 :
    print('입력 오류')
    sys.exit(0) # 종료

if argv[0] == 'mul':
    print(int(argv[1]) * int(argv[2]))
elif argv[0] == 'add':
    print(int(argv[1]) + int(argv[2]))


# if len(argv) <= 2 or len(argv) >= 4 :
#     print('입력 오류')
# elif argv[0] == 'mul':
#     print(int(argv[1]) * int(argv[2]))
# elif argv[0] == 'add':
#     print(int(argv[1]) + int(argv[]))
# else :
#     print('입력 오류')

# 빈 배열이면 for문을 돌지 않아서 for문 자체가 실행되지 않음.