import os

os.chdir("C:/Users/kimhi/python-test")
dir = os.popen('git status')
print(dir.read())
print(os.listdir())


# 타자 연습 게임
import random
import time

word= ['sky', 'earth', 'moon', 'flower', 'tree', 'apple', 'grape', 'garlic', 'onion', 'potato']
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