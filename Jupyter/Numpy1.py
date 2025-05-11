# %%
print('hello')

# %%
print('shift + enter = 다음줄로 넘기기')

# %%
print('esc => d 두번, 삭제하기입니다!')

# %%
print('Hello world')

# %%
a = 1
a

# %%
b = [1,2,3,4,5]

# %%
print(b*2)

# %%
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

# %%
import numpy as np 
x = np.array([3,1,2,'1'])
print(x)
print(([3,1,2,'1']))
print(type(x))
print(type([3,1,2]))

# %%
c = [[1],[1,2]]
# d = np.array([[1],[1,2]]) 오류
d = np.array([[1,1],[1,2]])

for x,y in d:
    print(x,y)

# %%
# %ls

# %%
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])

print(x+y)
print(x-y)
print(x*y)
print(x/y)

# %%
x = np.array(['1.0', '2.0', '3.0'])
y = np.array(['2.0', '4.0', '6.0'])

print(x+y)
print(x-y)
print(x*y)
print(x/y)

# %%
print(x.shape)
print(x.dtype)
print(d.shape)
print(y/2.0)

# %%
print(x.ndim)

# %%
a = np.array([[1,2],[3,4],[5,6]])
print(a.ndim)

# %%
print(a.shape)

# %%
a = np.array([[[1],[2]],[[3],[4]],[[5],[6]]])
print(a.ndim)

# %%
print(a.shape)

# %%
a = np.array([[[1,2],[2,2]],[[3,2],[4,2]],[[5,2],[6,2]]])
print(a.ndim)

# %%
print(a.shape)

# %%
np.dot(4,2)

# %%
ndar1 = np.array([1,2])
ndar2 = np.array([4,5])
np.dot(ndar1,ndar2)

# %%
ndar1 = np.array([[1,2],[3,4]])
ndar2 = np.array([[1,2],[3,4]])
np.dot(ndar1,ndar2)

# %%
ndar1 = np.array([[1],[3]])
ndar2 = np.array([[1,2],[3,4]])
np.matmul(ndar1,ndar2)

# %%
ndar2 = np.array([[[1],[2]],[[3],[4]]])
print(ndar2.shape)
a = ndar2.flatten()
print(a.ndim)
print(ndar2)
print(a)

# %%
ndarr = np.array([[1,2],[2,3],[3,4]])
ndarr.reshape(2,3)

# %%
ndarr.reshape(6,1)

# %%
ndarr.reshape(1,6)

# %%
ndarr.flatten() # 1차원?

# %%
np.random.randint(5,size=(2,4))

# %%
np.random.rand(2,4)

# %%
rng = np.random.default_rng() # 권장장

# %%
rng.random()

# %%
rng.integers(0,10,(2,4))

# %%
ndarr = np.array([[6,3],[5,2],[4,1]])
ndarr > 4

# %%
ndarr[ndarr > 1] # 1차원

# %%
ndarr[1:]

# %%
ndarr[[[ True, True],
       [ True, True],
       [True, False]]]

# %%
import numpy as np

ex = np.zeros(10)
# ex = [0 for i in range(10)]
print(ex)

# %%
ex[4] = 1
print(ex)

# %%
ex1 = np.arange(10,31)
print(ex1)

# %%
rng = np.random.default_rng()
print(rng.integers(0,100,(2,2)))

# %%
k = np.random.rand(2,4)
print(k)

# %%
k2 = rng.random((2,4))
print(k2)

# %%
arr1 = np.arange(35,75)
# arr1.shape = (10,4) or
arr2 = arr1.reshape(10,4)
print(arr2)


# %%
print(arr2[::-1]) # 역순으로 끝까지 출력.

# %%
print(arr2[1:9,2::])
# print(arr2[1:-1, 2:])

# %%
print(arr2[:,3]) # 정수 인덱스 => 1차원
# arr2[:, -1]
print(arr2[:,3:4]) # 범위 인덱스 = > 2차원
# arr2[:, -1:]

# %%
arr3 = arr2[:,3:4]
# arr2[::-1,-1:]
print(arr3[::-1])

# %%
arr4 = rng.integers(1,51,(5,6))
# arr4 = rng.integers(1,51, size = (5,6))
arr5 = [j  for i in arr4  for j in i  if j%2 == 0 ]
# arr4[arr4%2 == 0]
print(arr4)
print('짝수만 출력 : ',arr5)


