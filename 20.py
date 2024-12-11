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


import calendar

calendar.prcal(2024)
calendar.prmonth(2024,12)
print(calendar.weekday(2024,12,11)) # 요일을 숫자로 알려줌

days = ['월', '화', '수', '목', '금', '토', '일']
weekday = datetime.date.today().weekday()
print('오늘은 '+days[weekday]+'요일')

weekday = datetime.date(2025,12,25).weekday()
print('크리스마스는 '+days[weekday]+'요일')

def getWeekday(yyyy,mm,dd) :
    weekday = datetime.date(yyyy,mm,dd).weekday()
    print(f'{yyyy}년 {mm}월 {dd}일은 {days[weekday]}요일')

getWeekday(2024,12,24)

import time

a = time.time()
time.sleep(2)
b = time.time()
print(b-a)

print(time.localtime())
time_str = time.localtime()
print(time_str.tm_year)

print(time.ctime())


# 1970.1.1 이후 기준
year = round(time.time()/(365*24*60*60))
print(year)
print(time.time()/(365*24*60*60))

day = time.time()/(24*60*60)
print(day)


start = time.time()

for i in range(10):
    print(i)
    time.sleep(1)

end = time.time()
print(f'수행 시간 : {end-start}초')

def check_time(func) :
    start = time.time()
    func()
    end = time.time()
    print(f'수행 시간 : {end-start}초')

def a() :
    for i in range(10):
        print(i)
        time.sleep(1)

def b() :
    for i in range(100):
        print(i)
        time.sleep(0.5)

check_time(a)