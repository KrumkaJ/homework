def my_func(num_1, num_2, num_3):
    my_num = [num_1, num_2, num_3]
    max_numbers = []
    for numb in my_num:
        number = max(my_num)
        max_numbers.append(number)
        my_num.remove(number)
    print(sum(max_numbers))


my_func(34, 5, 18)

