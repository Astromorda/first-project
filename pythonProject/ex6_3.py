print('Введите числа A и B при условии, что A <= B')
a = int(input('Введите число A: '))
b = int(input('Введите число B: '))
k = 0
if a <= b:
    i = a
    while i <= b:
        if i % 2 == 0:
            k += 1
        i += 1
    print('Кол-во четных чисел на заданном отрезке =', k, sep=' ')
else:
    print('A должно быть <= B')