my_str = input('Введите несколько слов через пробел: ')

my_list = my_str.split()

for i, el in enumerate(my_list, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f'{i}. {el}')