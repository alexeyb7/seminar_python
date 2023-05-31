# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

number = int(input("Введите максимум чисел: "))
num = []
for i in range(number):
    num.append(random.randint(1, number))
print(num)

x = int(input("Введите число: "))

if num.count(x) != 0:
    print("Число", x, " в массиве встречается ", num.count(x), " раз")
else:
    #    i = 0
    #    while i < number - 1:
    #        if (abs(x - num[i])) > (abs(x - num[i + 1])):
    #            near = num[i + 1]
    #        near = num[i]
    #        i += 1
    near = min([abs(x - num[i])])

print("Ближайший к числу элемент массива", near)
