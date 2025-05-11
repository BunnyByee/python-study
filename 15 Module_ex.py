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

import module_ex.cm2
print(module_ex.cm2.add(1,2))