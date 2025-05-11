# 실습 1
class Calc :
    def __init__(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2
        print(f'num1 : {n1}, num2 : {n2}')
    
    def add(self) :
        print(f'add : {self.__n1 + self.__n2}')
    
    def sub(self) :
        print(f'sub : {self.__n1 - self.__n2}')
    
    def mul(self) :
        print(f'mul : {self.__n1 * self.__n2}')
    
    def div(self) :
        if self.__n2 == 0 :
            print('0으로 나누기는 불가')
        else:
            print(f'div : {self.__n1 / self.__n2}')
        
a = Calc(10,2)
a.add()
a.sub()
a.mul()
a.div()

b = Calc(4,0)
b.add()
b.sub()
b.mul()
b.div()

class Employee :
    serial_num = 1000

    def __init__(self, name):
        Employee.serial_num += 1
        self.id = Employee.serial_num
        self.name = name
    
    def __str__(self):
        return f'사번 : {self.id}, 이름 : {self.name}'
    
e1 = Employee("최사원")
print(e1)

e2 = Employee("안사원")
print(e2)

e3 = Employee("한사원")
print(e3)

employee = [Employee('구름'), Employee('별'), Employee('행성'), Employee('달')]

for i in employee :
    print(i)

# 실습 2
class Supermarket :
    count = 0

    def __init__(self, location, name, product, customer):
        Supermarket.count += 1
        self.__location = location # 위치
        self.__name = name # 가게 이름
        self.__product = product # 파는 물건
        self.__customer = customer # 손님 수

    def print_location(self) :
        print(f'가게 위치: {self.__location} \n')

    def change_category(self,k) :
        self.__product = k
    
    def show_list(self) :
        print(f'파는 물건: {self.__product} \n')

    def enter_customer(self) :
        self.__customer += 1

    def show_info(self) :
        print(f'가게 이름 : {self.__name}, 가게 위치 : {self.__location}')
        print(f'파는 물건 : {self.__product}, 손님 수 : {self.__customer} \n')
    
    def show_supermarket_count():
        print(f'인스턴스 개수 : {Supermarket.count} \n')

a = Supermarket('응암','@@과일','바나나',50)
b = Supermarket('역촌','$$채소가게','호박',70)

a.print_location()
a.show_list()
a.change_category('딸기')
a.show_list()
a.enter_customer()
a.show_info()
Supermarket.show_supermarket_count()