with open('./output/input.txt','a') as f:
    while True :
        text = input('저장할 내용을 입력해 주세요(종료-z) : ')
        if text == 'z' or text == 'Z':
            break
            # sys.exit(0)
        f.write(text)
        f.write('\n')