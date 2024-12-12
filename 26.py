# 실습 3
dictUser = {}

with open('member.txt', 'r') as f:
    for i in f :
        n , p = i.split()
        dictUser[n] = p

dictTel = {}    

with open('member_tel.txt', 'r') as f:
    for i in f :
        n , t = i.split()
        dictTel[n] = t

# 3명의 회원에 대한 이름, 비밀번호 입력 받기
name = input('이름을 입력하세요. : ')
pw = input('비밀번호를 입력하세요 : ')

if pw == dictUser.get(name) :
    print('로그인 성공')
    tel = input('전화번호를 입력하세요 : ')
    with open('member_tel.txt', 'r+') as f:
            if name in dictTel:
                dictTel[name] = tel
            else :
                with open('member_tel.txt', 'a') as f:
                    f.write(f'{name} {tel}\n')
else :
    print('로그인 실패')