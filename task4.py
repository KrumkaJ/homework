number = int(input('Введите целое положительное число: '))
max_numb = number % 10
number = number // 10
while number > 0:
    if number % 10 > max_numb:
        max_numb = number % 10
    number = number // 10
print(f'Максимальное цифра в числе {max_numb}')
