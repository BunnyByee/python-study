# 실습 5
numbers = input("숫자 여러 개 입력 > ").split()
numbers = [int (n) for n in numbers]
print(numbers)

max_n = max(numbers)
min_n = min(numbers)

print(f"가장 큰 값: {max_n}")
print(f"가장 큰 값: {min_n}")

hap = 0
for i in numbers :
    hap += i
hap = hap - (max_n + min_n)
count = len(numbers) - 2

print(f"나머지 값의 평균 = {hap/count}")




