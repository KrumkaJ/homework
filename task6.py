def int_func(words):
    return words.title()


my_word = input('Введите слово из маленьких латинских букв: ')
print(int_func(my_word))

my_str = input('Введите несколько слов из маленьких латинских букв через пробел: ')
print(int_func(my_str))
