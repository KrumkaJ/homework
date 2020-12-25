my_list = [9, 7, 7, 4, 2]
print(my_list)

number = int(input('Введите натуральное число: '))

for i in range(len(my_list)):
    if my_list[i] == number:
        my_list.insert(i + 1, number)
        break
    elif my_list[0] < number:
        my_list.insert(0, number)
        break
    elif my_list[1] < number:
        my_list.insert(1, number)
        break
    elif my_list[3] < number:
        my_list.insert(3, number)
        break
    elif my_list[4] < number:
        my_list.insert(4, number)
        break
    elif my_list[4] > number:
        my_list.insert(4 + 1, number)
        break

print(my_list)