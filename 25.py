# # 실습 2
# for i in range(3):
#     # 3명의 회원에 대한 이름, 비밀번호 입력 받기
#     name = input('이름을 입력하세요. : ')
#     pw = input('비밀번호를 입력하세요 : ')
#     check_txt = f'{name} {pw}\n'

#     # 리스트 만들기    
#     with open('member.txt', 'r') as f2:
#         member_txt = f2.readlines()

#     if member_txt[i] == check_txt :
#         print('로그인 성공\n')
#     else :
#         print('로그인 실패\n')
    
#     check_txt = ''

# # 실습 2 ver2
# # 3명의 회원에 대한 이름, 비밀번호 입력 받기
# name = input('이름을 입력하세요. : ')
# pw = input('비밀번호를 입력하세요 : ')
# check_txt = f'{name} {pw}\n'

#     # 리스트 만들기    
# with open('member.txt', 'r') as f2:
#     for i in f2 :
#         if i == check_txt :
#             print('로그인 성공\n')
#             break
#         else :
#             print('로그인 실패\n')
#             break

# 실습 2 ver3 딕셔너리 활용
dictUser = {}    

with open('member.txt', 'r') as f:
    for i in f :
        n , p = i.split()
        dictUser[n] = p

# 3명의 회원에 대한 이름, 비밀번호 입력 받기
name = input('이름을 입력하세요. : ')
pw = input('비밀번호를 입력하세요 : ')

if pw == dictUser.get(name) :
    print('로그인 성공')
else :
    print('로그인 실패')
