# # 실습 1
# class Calc :
#     def __init__(self, n1, n2):
#         self.__n1 = n1
#         self.__n2 = n2
#         print(f'num1 : {n1}, num2 : {n2}')
    
#     def add(self) :
#         print(f'add : {self.__n1 + self.__n2}')
    
#     def sub(self) :
#         print(f'sub : {self.__n1 - self.__n2}')
    
#     def mul(self) :
#         print(f'mul : {self.__n1 * self.__n2}')
    
#     def div(self) :
#         if self.__n2 == 0 :
#             print('0으로 나누기는 불가')
#         else:
#             print(f'div : {self.__n1 / self.__n2}')
        
# a = Calc(10,2)
# a.add()
# a.sub()
# a.mul()
# a.div()

# b = Calc(4,0)
# b.add()
# b.sub()
# b.mul()
# b.div()

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