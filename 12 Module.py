import modules.calc_module as calc_module

print(calc_module.add(1,2))
print(calc_module.sub(1,2))
print(calc_module.mul(1,2))
print(calc_module.div(1,2))


# 특정 함수만 import
from modules.calc_module import add
print(add(1,2))
# calc_module.add() # 안됨

# 모듈명 간단하게 바꿔서 사용 가능
import modules.calc_module as cm
print(cm.add(1,2))


import math
print(math.floor(3.141592))
print(math.ceil(3.141592))
print(math.sqrt(9))

from math import floor, ceil
print(floor(3.141592))
print(ceil(3.141592))


import random
print(random.randint(1,5))
print(random.uniform(1,2))
print(random.random())
print(random.randrange(1,3))
print(random.randrange(1,5,2))


import random
com = random.randint(1,100)

min_v = 1
max_v = 100

i = 0
score = 100

while i < 10 :
    try:
        guess = int(input('숫자 입력([%d회]%d ~ %d): ' % (i+1, min_v, max_v)))
        i += 1

        if guess < 0 or guess > 100 :
            print('입력 범위를 초과했어요')
        elif com == guess :
            print('정답이에요!!')
            print(f'정답 : {com}')
            print(f'점수 : {score - (i)*10}점')
            break
        elif com > guess:
            print('랜덤수보다 작아요')
            min_v = guess
        else:
            print('랜덤수보다 커요')
            max_v = guess
    except ValueError:
        print('숫자만 입력 가능합니다.')


# for i in range(1,11) :
#     print(f'숫자 입력([{i}회] {min_v} ~ {max_v}): ',end='')
#     a = int(input())


#     if com == a :
#         print('정답이에요!')
#         print(f'정답 : {com}')
#         print(f'점수 : {score - (i-1)*10}')
#         quit()
#     elif com < a :
#         max_v = a
#         print('랜덤수보다 커요')
#     elif com > a :
#         min_v = a
#         print('랜덤수보다 작아요')