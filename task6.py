# Структура данных "Товары"
products = int(input('Введите количество товаров, которые вы хотите купить: '))
number = 1
products_list = []
products_dict = []

while number <= products:
    my_dict = {
        'Название': input('Ведите название товара: '),
        'Цена': input('Введите цену товара: '),
        'Kоличество': input('Введите количество товара: '),
        'Ед': input('Введите единицу измерения товара: ')
    }
    products_dict = my_dict
    products_list.append((number, products_dict))
    number += 1

print(products_list)

# Аналитика товаров
analytics = {}

for good in products_list:
    for key, val in good[1].items():
        if key in analytics:
            analytics[key].append(val)
        else:
            analytics[key] = [val]

print(analytics)
