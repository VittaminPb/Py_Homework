# Реализуйте алгоритм перемешивания списка.

import random 
 
rndList = []
for i in range(10):
    rndList.append(random.randint(0, 20)) 
print(rndList)
 
random.shuffle(rndList)
print(rndList)