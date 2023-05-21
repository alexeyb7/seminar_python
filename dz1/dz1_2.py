# Задача 2: Найдите сумму цифр трехзначного числа.
in_str = input("Введите трехзначное число: ")
in_digit = int(in_str)
if (in_digit < 100) or (in_digit > 1000):
    print("Повторите ввод")
else:
    out_digit1 = in_str[0]
    out_digit2 = in_str[1]
    out_digit3 = in_str[2]
    print("Сумма цифр числа:", int(out_digit1) + int(out_digit2) + int(out_digit3))
