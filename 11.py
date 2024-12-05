d = [[10,20],[30,40],[50,60]]

print(d)

print(d[0][0])
print(d[1][1])

d.append([70,80])
print(d)

d[0][0] = 90
print(d)

d[1].pop() # 하나 삭제 되면 x,y for문 못함
# del d([1][1])
print(d)
# print(d[1][1])

print(len(d))
print(len(d[0]))

for i in range(0, len(d)) :
    for j in range(0, len(d[i])) :
        print(d[i][j], end=" ")
    print()

for x,y in d :
    print(x,y)

dan = [
    [3,1],
    [3,2],
    [3,3],
    [3,4],
    [3,5],
    [3,6],
    [3,7],
    [3,8],
    [3,9]
]

for x, y in dan :
    print(f'{x} x {y} = {x*y}')

for i in range(len(dan)) :
    print(f'{dan[i][0]} x {dan[i][1]} = {dan[i][0] * dan[i][1]}')

# 추가 방법
for i in dan :
    print(f'{i[0]} x {i[1]} = {i[0]*i[1]}')