from modules.mylib import food

print(food.name)
food.cook()
food.eat()

# import modules.mylib.food
# modules.mylib.food.cook()

from modules.mylib.food import name, cook, eat
print(name)
cook()
eat()

import bbb.cm2
print(bbb.cm2.add(1,2))