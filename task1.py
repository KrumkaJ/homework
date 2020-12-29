def my_func():
    """
    Функция деления
    :return: возращает результат от деления двух чисел
    """
    try:
        numb_1 = int(input('Введите первое число: '))
        numb_2 = int(input('Введите первое число: '))
        return numb_1 / numb_2
    except ZeroDivisionError:
        print('Делить на ноль нельзя!')
    except ValueError:
        print('Введено не число!')


print(my_func())