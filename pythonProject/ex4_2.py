ch = int(input('Введите положительное пятизначное число: '))
a = ch // 10000
b = ch // 1000 % 10
c = ch // 100 % 10
d = ch // 10 % 10
e = ch % 10
z = float(d ** e * c / (a - b))
print(z)



# a, b, c, d, e = map(float, input('Введите пятизначное число через пробелы: ').split())
# z = d ** e * c / (a - b)
# print(z)