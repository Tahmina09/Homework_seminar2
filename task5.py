# 5. Реализуйте алгоритм перемешивания списка.

import random

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number_list)

for k in range(len(number_list)):
    i = random.randint(0, 9)
    j = random.randint(0, 9)
    number_list[i], number_list[j] = number_list[j], number_list[i]

print(number_list)