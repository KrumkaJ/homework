result = 0
special_character = False
while special_character == False:
    numbers = input('Введите несколько чисел через пробел или специальный символ "w" для завершения: ')
    my_list = numbers.split()
    my_sum = 0
    for num in my_list:
        if num == 'w':
            special_character = True
            break
        else:
            result += float(num)
    result += my_sum
    print(f'Сумма {result}')
print(f'Ваша сумма {result}. Вычисления закончены.')
