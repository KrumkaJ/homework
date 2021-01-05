my_list = [5, 76, 6, 14, 3, 28, 342, 4, 1, 45, 99]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(f'Исходный список: {my_list}')
print(f'Новый список: {new_list}')
