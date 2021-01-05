my_list = [3, 45, 6, 41, 3, 45, 653, 3, 15, 45, 99, 32, 87, 6]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f'Исходный список: {my_list}')
print(f'Новый список: {new_list}')
