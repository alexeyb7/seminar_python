"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
s = int(input("Введите сумму S:"))
p = int(input("Введите произведение P:"))
y = 1
while p != (s * y - y * y) and y <= 1000:
    y += 1

x = s - y
if (x >= 1) and (x <= 1000):
    print(x, y)
else:
    print("Повторите ввод")
