my_list = []
while list:
    words = input('Введите текст, для выхода нажмите пробел: ')
    if words == ' ':
        print(my_list)
        exit()
    else:
        word = words + '\n'
        my_list.append(word)

    with open('first.txt', 'w', encoding='utf-8') as my_f:
        my_f.writelines(my_list)
