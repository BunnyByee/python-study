import random
import time
import os

if os.path.exists('word.txt') : # 파일 존재 여부 확인

    with open('word.txt', 'r') as f:
        word = f.read().split() #전역 변수
else :
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 
            'apple', 'grape', 'garlic', 'onion', 'potato']

n = 1

input('[타자게임] 준비되면 엔터!')
start = time.time()

while n <11 :
    print('문제',n)
    question = random.choice(word)
    print(question) # 문제 출제
    user = input()
    if question == user :
        print('통과!!')
        n += 1 # 다음 문제 카운트
    else:
        print('오타! 다시 도전!')

end = time.time()
et = end - start
print(f'타자 시간: {et: .2f}초')