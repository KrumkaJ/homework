with open('second.txt', 'r', encoding='utf-8') as my_f:
    lines = 0
    for line in my_f:
        flag = 0
        word = 0
        for el in line:
            if el != ' ' and flag == 0:
                word += 1
                flag = 1
            elif el == ' ':
                flag = 0
        lines += 1
        print(f'В сторе {word} слов')

    print(f'Всего сток {lines}')
