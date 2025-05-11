f = open("text.txt","w")
f.write("Hello World \n")
f.close()

f2 = open('text.txt')
# 같은 명의 파일이 있는경우 W 불가능
print(f2.read())
f2.close()

# close 무조건!
# EOF end of file

f3 = open('text.txt', 'a')
f3.write('I am so hungry now \n')
f3.close()

f4 = open('text.txt')
# print(f4.readline(), end="")
# print(f4.readline(), end="")
print(f4.readlines())
f4.close()

f5 = open("text.txt","r+")
print(f5.read())
print(f5.tell()) # 문자열 \n 뒤에 윈도우개행문자 \r이 추가됨
f5.seek(4) # 처음으로 이동
print(f5.write('8'))
f5.close()

f6 = open('text2.txt',"r+")
str6 = f6.read()
print(f6.tell())
f6.seek(str6.find('5'))
print(f6.write("8"))
f6.close()

with open('text2.txt',"r+") as f7 :
    str6 = f7.read()
    print(f7.tell())
    f7.seek(str6.find('4'))
    print(f7.write("8"))
# f.close() 필요 X