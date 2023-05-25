﻿"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
"""


s = input("Введите номер билета : ")

if int(s) >= 1000000 or int(s) < 100000:
    print("Повторите ввод")
else:
    if (int(s[0]) + int(s[1]) + int(s[2])) == (int(s[3]) + int(s[4]) + int(s[5])):
        print("Билет счастливый!")