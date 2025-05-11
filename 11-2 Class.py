class Movie :
    count = 0
    # 함수는 기본적으로 public
    def __init__(self, title, audience):
        self.__title = title
        self._audience = audience
        Movie.count += 1
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
    
    def get_audience(self):
        return self._audience

movie1 = Movie('파묘', 100)
# print(movie1.__title) # 오류 발생
print(movie1.get_title())
# movie1.__title = '오겜' # __는 직접 접근 못함.
# print(movie1.get_title())
# print(movie1.__title)
print(movie1._audience)
print(movie1.get_audience())

class MyAdd:
    __a = 1
    __b = 2

    def sum(self) :
        return self.__a + self.__b
    
    def change(x) :
        MyAdd.__a = x

a = MyAdd()
print(a.sum()) # 3
# __a 값 3으로 변경 
MyAdd.change(3)
print(a.sum()) # 5

class Health :
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
    
    def getname(self):
        return self.__name
    
    def sethp(self, hp):
        hp = max(hp, 0)
        hp = min(hp, 100)
        # if hp < 0 :
        #     hp = 0
        # elif hp > 100 :
        #     hp = 100
        self.__hp = hp
    
    def gethp(self) :
        return "hp : " + str(self.__hp)

    def exercise(self, hours):
        self.sethp(self.__hp + hours)
        print(f"{hours}시간 운동하다")
    
    def drink(self, cups):
        self.sethp(self.__hp - cups)
        print(f"술을 {cups}잔 마시다")

p1 = Health('나몸짱')
p1.sethp(100)
p1.exercise(5)
p1.drink(2)
print(f'{p1.getname()} - {p1.gethp()}')

p2 = Health('나약해')
p2.sethp(10)
p2.exercise(1)
p2.drink(12)
print(f'{p2.getname()} - {p2.gethp()}')