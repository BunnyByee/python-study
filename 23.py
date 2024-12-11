# f = open("text.txt","w")
# f.write("Hello World \n")
# f.close()

# f2 = open('text.txt')
# # 같은 명의 파일이 있는경우 W 불가능
# print(f2.read())
# f2.close()

# # close 무조건!
# # EOF end of file

# f3 = open('text.txt', 'a')
# f3.write('I am so hungry now \n')
# f3.close()

f4 = open('text.txt')
print(f4.readline(), end="")
print(f4.readline(), end="")
f4.close()
