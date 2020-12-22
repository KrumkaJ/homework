proceeds = int(input('Введите объем выручки: '))
costs = int(input('Введите объем издержек: '))

if proceeds > costs:
    print('У вашей фирмы прибыль')
    profit = proceeds - costs
    print(f'Рентабельность вашей выручки составляет: {profit / proceeds:.2f}')
    worker = int(input('Ведите численность сотрудников вашей фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника составляет: {profit / worker:.2f}')
else:
    print('У вашей фирмы убыток')
