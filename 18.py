# class Country :
#     def __init__(self, name, population, capital):
#         self.name = '나라 이름'
#         self.population = '인구'
#         self.capital = '수도'

#     def show(self) :
#         print("국가 클래스의 메소드")

# class Korea(Country) :
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print('국가 이름: ',self.name) # 오버라이딩

# country = Korea('대한민국')
# country.show()
# print(country.name)
# # country.show_name()

# 실습 3
class Calculator() :
    def __init__(self):
        self.value = 100

    def sub(self, value) :
        self.value -= value
    

class MinLimitCalculator(Calculator) :
    def __init__(self): # 이거는 없어도 됨!
        super().__init__() 
    
    def sub(self, value):
        self.value -= value
        if self.value < 0 :
            self.value = 0

        # super().sub(value)
        # self.value = max(0, self.value)

        # self.value = max(0, self.value - value) # 가장 최적화!

cal = MinLimitCalculator()
cal.sub(20)
cal.sub(90)
print(cal.value) # 0 출력

# 파이썬은 오버로딩이 안 됨! 