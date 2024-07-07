n = int(input('Введите кол-во чисел: '))
k = 0
for i in range(n):
    a = int(input()) # вводится число
    if a == 0:
        k += 1
print()
print(k, 'число/чисел равно нулю')