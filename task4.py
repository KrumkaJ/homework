# возведение в степень с помощью оператора **
def my_func(num_1, num_2):
    return num_1 ** num_2


print(my_func(16, -3))


# использование цикла
def my_func_2(num_3, num_4):
    result = 1
    for i in range(abs(num_4)):
        result *= num_3       # result = result * num_3
    if num_4 >= 0:
        return result
    else:
        return 1 / result


print(my_func_2(7, -2))
