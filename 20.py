# 실습 - 로또번호
import random

a = set()

while True :
    a.add(random.randint(1,45))

    if len(a) == 6 :
        break

b = list(a)
b.sort()
print(b)

import datetime

now = datetime.datetime.today()

print(now)
print(now.year, now.month)

print(f'{now.hour}시 {now.minute}분 {now.second}초')

today = datetime.date.today()
print(today)
# print(today.hour) # 안됨

print('지금까지 몇 일?')
first_day = datetime.date(2024,11,25)
print(first_day)

today = datetime.date.today()
print(today)

passed_time = today - first_day
print(passed_time)

print(f'개강 이후 {passed_time.days}일 지났습니다.')



