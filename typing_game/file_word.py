import random

with open('word.txt', 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree', 
            'apple', 'grape', 'garlic', 'onion', 'potato']

    for i in word :
        f.write(i + ' ') # \n, \r, \t 등 사용 가능

with open('word.txt', 'r') as f:
    data = f.read().split()
    # data = f.readlines() # \n일 경우 사용가능
    word = random.choice(data)
    print(word)