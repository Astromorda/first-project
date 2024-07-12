N = int(input("Введите кол-во строк <= 10e9 по модулю: "))
numbers = []

if abs(N) <= 10e5: # проверяем, что введенное число по модулю <= 10e9
    for i in range(N):
        while True: # пока словие не выполнится, дальше не двинется
            number = input(f"Введите {i+1}-е однозначное число: ")
            # длина символа = 1 или содержит минус, но два символа
            if (len(number)) == 1 or (('-' in number) and (len(number)) == 2):
                numbers.append(number) # каждый введенный символ добавляется в конец списка
                print(numbers)
                break # выход из условия, если условие не выполнено
            else:
                print("Вы ввели неоднозначное число")
    revers_numbers = list(reversed(numbers)) # список перевернулся и записался в новый список
    print(revers_numbers)
else:
    print("Вы ввели слишком большое кол-во строк")

