stroka = input("Введите строку: ")
mas = []
l = len(stroka)

if len(stroka) <= 1000:
    for i in stroka[:l:1]: # range(len(stroka)):
        mas.append(i)

    for i in range(l-1):
    # for (i, elem) in enumerate(mas):
        if (mas[i] == ' ') and (mas[i] == mas[i+1]):
            mas[i] = ''

    print(f'Преобразованная строка: [{(''.join(mas))}]')
else:
    print("Вы ввели строку длинее 1000 символов")