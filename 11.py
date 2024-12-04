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
