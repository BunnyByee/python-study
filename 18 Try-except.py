try :
    num = int(input('정수 입력:'))
except ValueError:
    print('정수가 아님')

# num = int(input('정수 입력:'))
# try ~ except가 없으면 에러가 발생할 수 있음.


try :
    num = int(input('정수 입력:'))
except ValueError as msg:
    print(msg)
    # 무슨 에러인지 출력할 수 있음


try :
    num = int(input('정수 입력:'))
except :
    print('정수가 아님!')


try :
    num = int(input('정수 입력:'))
except ValueError as msg: # 오류가 ValueError일시 얘가 먼저 실행됨.
    print('ValueError',msg)
except Exception as msg : # 최상단, 최대한 밑에 배치하는 것이 좋음.
    print('Exception',msg)
else :
    print('예외 없음')


# 실습 1
while True :
    try :
        num = int(input('숫자 입력 : '))
        print('정수 입력 성공 : ',num)
        break
    except ValueError :
        print('정수가 아님! 정수를 입력해주세요!')

while True :
    try :
        num = int(input('숫자 입력 : '))
        break
    except ValueError :
        print('정수가 아님! 정수를 입력해주세요!')
        continue
    finally : # try ~ except 구문을 벗어날 때 무조건 실행됨.
        print('무조건무조건이야야')
print('정수 입력 성공 : ',num)


a = 1
try :
    a+=1
    if a > 1: # 코딩할 때 에러 찾고 싶을때 사용
        raise Exception
    a+= 2
    print('a',a)
except:
    print('error',a)

class Animal :
    def breathe(self) :
        print('숨숴')
    def cry(self) :
        raise NotImplementedError
    # 특정 상황에서 강제로 뛰어넘고 싶을때 사용!

class Dog(Animal) :
    def cry(self) :
        print('멍멍')

d = Dog()
d.breathe()
d.cry()