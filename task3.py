employee = []
elem = []
with open('third.txt', 'r', encoding='utf-8') as my_f:
    for line in my_f:
        new_line = line.rstrip('\n')
        el = new_line.split(' ')
        if float(el[1]) < 20000.00:
            employee.append(el[0])
        elem.append(el[1])

print(f'Сотрудники с окладом меньше 20000.00: {employee}')
print(f'Средняя величина доходов: {sum(map(float, elem)) / len(elem)}')
