numbers = ['Один', 'Два', 'Три', 'Четыре']
new_list = []

with open('fourth.txt', 'r', encoding='utf-8') as my_f:
    for line in my_f:
        new_line = line.rstrip('\n')
        el = new_line.split(' ', 1)
        new_list.append(numbers[0] + '  ' + el[1] + '\n')
        numbers.pop(0)
    print(new_list)

with open('fourth_new.txt', 'w', encoding='utf-8') as my_f:
    my_f.writelines(new_list)
