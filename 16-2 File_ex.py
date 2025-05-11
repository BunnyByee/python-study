# 실습 1
n = 1

with open('member.txt', 'w') as f:
    while n < 4 :
        # 3명의 회원에 대한 이름, 비밀번호 입력 받기
        name = input('이름 : ')
        pw = input('비밀번호 : ')
        
        # 사용자로부터 입력된 정보를 기록
        f.write(f'{name} {pw}\n')

        n += 1
    
with open('member.txt', 'r') as f:
    # 텍스트 파일에 저장된 회원명부 출력
    print(f.read())