class Movie:
    title = "범죄도시4"

movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)

movie1.title = "파묘"
print(movie1.title)
print(movie2.title)

movie1.score = "1" # 정의와 동시에 생성
print(movie1.score)
# print(movie2.score) # score가 클래스에 정의되어 있지 않기때문에 오류 발생


class Movie:
    name = ''
    def print_msg(msg) :
        print(msg)
    def modify(self, movie) :
        self.name = movie
    def print_name(self):
        print(self.name)

movie1 = Movie()
movie2 = Movie()

Movie.print_msg("print하기")
# Movie.modify(movie1, "print하기2")
movie1.modify('print하기3')
# ↑=> movie1.name = '프린트하기3'
movie1.print_name()
movie2.modify('print하기4')
print("movie2.name",movie2.name)
# movie1.print_msg('ttt') # 1개 인수에 2개 제공. 


class Movie:
    def __init__(self):
        print("Hello")

movie = Movie()


class Movie1 :
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience

movie1 = Movie1("파묘", 100)
movie2 = Movie1("파묘2", 200)

print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)

# def __init__(self, title = "오징어게임", audience=300) :
# movie3 = Movie1()
# print(moive3.title, movie3.audience)


class Movie2 :
    count = 0
    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie2.count += 1

movie1 = Movie2("파묘", 100)
print(Movie2.count) # 1
movie2 = Movie2("파묘2", 200)

print(movie1.count) # 2
print(movie2.count) # 2
print(Movie2.count) # 2

Movie2.count += 1 
print(movie1.count) # 3
print(movie2.count) # 3
print(Movie2.count) # 3

movie1.count += 1 # 이건 별로 안 좋은 코드.
print(movie1.count) # 4
print(movie2.count) # 3
print(Movie2.count) # 3

Movie2.count += 1 
print(movie1.count) # 4
print(movie2.count) # 4
print(Movie2.count) # 4