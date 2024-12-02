# # 과제1

# n = int(input("정수 입력 : "))
# n_list = []
# for i in range (1,n+1) :
#     n_list.append(i)
# print(n_list)

# print(n_list[0::2]) # 홀수
# print(n_list[1::2]) # 짝수

# # 과제 2
# vending_machine = ['게토레이', '레쓰비', '생수', '이프로']
# juice = input("마시고 싶은 음료? ")
# if juice in vending_machine :
#     print(f"{juice} 드릴게요")
# else :
#     print(f"{juice}는 지금 없네요")

# 과제 3
vending_machine = ['게토레이', '게토레이', '레쓰비', '레쓰비', '생수', '생수', '생수', '이프로']
print("남은 음료수:",vending_machine,"\n")

user = input("사용자 종류를 입력하세요:\n 1.소비자\n 2.주인\n")

# 소비자일 경우,
if user == '1' or user == '소비자' :
    juice = input("마시고 싶은 음료? ")
    if juice in vending_machine : # 음료 제공 후 리스트에서 삭제
        print(f"{juice} 드릴게요")
        vending_machine.remove(juice)
        print("남은 음료수:",vending_machine,"\n")
    else :
        print(f"{juice}는 지금 없네요") # 없음

# 주인일 경우,
elif user == '2' or user == '주인'  : 
    work = input("할 일 선택(문자 입력):\n 1. 추가\n 2. 삭제\n")
    # 추가할 경우,
    if work == '1' or work == '추가'  :
        print("남은 음료수:",vending_machine,"\n")
        juice = input("추가할 음료수? ")
        if vending_machine.count(juice) != 0 : # 중복O => 위치에 값 추가
            vending_machine.insert(vending_machine.index(juice),juice)
        else : # 중복X => 새로 추가 후 정렬
            vending_machine.append(juice)
            vending_machine.sort()
        print("추가 완료")
        print("남은 음료수:",vending_machine,"\n")
    
    # 삭제할 경우,
    elif work == '2' or work == '삭제'  :
        print("남은 음료수:",vending_machine,"\n")
        juice = input("삭제할 음료수? ")
        if juice in vending_machine :
            vending_machine.remove(juice)
            print("삭제 완료")
            print("남은 음료수:",vending_machine,"\n")
        else :
            print(f"{juice}는 지금 없네요")

    # 입력한 값이 1, 2, 추가, 삭제가 아닐 경우
    else :
        print("입력을 잘못 하셨습니다.")

# 입력한 값이 1, 2, 소비자, 주인이 아닐 경우
else :
    print("입력을 잘못 하셨습니다.")
