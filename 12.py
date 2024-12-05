# def f(x) :
#     result= x**2 + 2*x +1
#     return result

# print(f(3))

# def sayHi():
#     print('안녕하세용')
#     print('hello')

# sayHi()

# x = 10 # 전역변수
# def func() :
#     x = 20 # 지역변수
#     print(x)

# func()
# print(x)

# def func2() :
#     print(x)

# func2()

# def func() :
#     x = 20
#     print("func",x)
#     func2()

# func()

# def func3(x) :
#     print("func",x)

# func3(3)

# # 실습 1
# def func(x,y) :
#     if x == y :# 두 수가 같으면
#         print(x*y) # 곱하기
#     else : # 아니면
#         print(x + y) # 더하기

# func(2,2)
# func(5,3)

def func2(x,y) :
    if x*y < 20000 :
        return x*y + 2500
    else :
        return x*y

print(f'상품 1의 가격: {func2(15000,2)}')
print(f'상품 2의 가격: {func2(6500,2)}')

def time(l) :
    l2 = [i* 2 for i in l]
    return set(l2)

v2 = time([1,2,3,4,5])
print(v2)

def sum_mul(a,b) :
    sum = a+b
    mul = a*b
    return sum, mul

s, m = (sum_mul(2,3))
print(s,m)