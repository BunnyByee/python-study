x = 2
print(1<x<5) # C : print(1 < x && x < 5)
print(True and False) # && => and
print(True or False) # || => or
print(not True) # ! => not

# in 연산자
cart = ["계란", "마늘", "콩나물", "커피"]
print('계란' in cart) # 리스트에 있으면 True
print('두부' in cart) # 리스트에 없으면 False

# if
if 1<3 : # True 면 다 실행, False면 들여쓰기 실행X
    print("True")
    print("True")
print("False")

# 실습 3
num = int(input("숫자 입력 : "))

if num%2 == 0 :
    print("짝수")
if num % 2 == 1 : # num % 2 != 0 이거도 있네! 
    print("홀수")
# 빠르게 실행하고 싶으면 비트 연산으로 리스트화 해서 하면 됨.

# if - else
if 1<3 : # True 면 True, False면 False
    print("True")
else:
    print("False")

# 실습 4
a = int(input("점수 입력 : "))

if a > 100 : 
    print("잘못 입력함")
elif a >= 90 : # 위에 if 삭제하고 if (90 <= a <= 100) :
    # a < 89 => 하나만 비교하기 때문에 효율적, 읽을때 헷갈릴 수는 있음. 
    print("A")
elif a >= 80 :
    print("B")
elif a >= 70 :
    print("C")
elif a >= 60 :
    print("D")
else :
    print("E")

# 실습 4 - 최적화된 코드
if a < 60 :
    print("E")
elif a < 70 :
    print("D")
elif a < 80 :
    print("C")
elif a < 90 :
    print("B")
else :
    print("A")

if a>100 :
    print("만점은 100, 잘못 입력함.")

# 실습 5
age = int(input("나이를 숫자로 입력해 주세요 : "))
if age < 1 :
    print("나이를 잘못 입력하셨습니다.") # 잘못 입력 => 종료
else : # 정상 입력 => 진행
    way = input("결제 방법을 입력해 주세요('카드' 또는 '현금'만 입력) : ")
    if way != '카드' and way != '현금' :
        print("결제 방법을 잘못 입력하셨습니다.") # 잘못 입력 => 종료
    else : # 정상 입력 => 진행
        if age < 8 :
            print(f"{age}세의 {way} 요금은 무료 입니다.")
        elif age < 14 :
            print(f"{age}세의 {way} 요금은 450원 입니다.")
        elif age < 20 :
            if way == '카드' :
                print(f"{age}세의 {way} 요금은 720원 입니다.")
            else :
                print(f"{age}세의 {way} 요금은 1000원 입니다.")
        elif age < 75 :
            if way == '카드' :
                print(f"{age}세의 {way} 요금은 1200원 입니다.")
            else :
                print(f"{age}세의 {way} 요금은 1300원 입니다.")
        else :
            print(f"{age}세의 {way} 요금은 무료 입니다.")

# 실습 5 수정
age = int(input("나이를 숫자로 입력해 주세요 : "))
if age < 1 :
    print("나이를 잘못 입력하셨습니다.") # 잘못 입력 => 종료
    age = int(input("다시 나이를 숫자로 입력해 주세요 : "))
else : # 정상 입력 => 진행
    way = input("결제 방법을 입력해 주세요('카드' 또는 '현금'만 입력) : ")
    if way != '카드' and way != '현금' :
        print("결제 방법을 잘못 입력하셨습니다.") # 잘못 입력 => 종료
        way = input("다시 결제 방법을 입력해 주세요('카드' 또는 '현금'만 입력) : ")
    else : # 정상 입력 => 진행
        if age < 8 :
            fee = '무료'
        elif age < 14 :
            fee = '450원'
        elif age < 20 :
            if way == '카드' :
                fee = '720원'
            else :
                fee = '1000원'
        elif age < 75 :
            if way == '카드' :
                fee = '1200원'
            else :
                fee = '1300원'
        else :
            fee = '무료'
            
print(f"{age}세의 {way} 요금은 {fee} 입니다.")

# DFS depth first search => 스택
# BFS => 큐