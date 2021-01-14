with open('fifth.txt', 'w') as my_f:
    my_line = '5 65 49 7 12 999'
    my_f.write(my_line)
    my_list = my_line.split()
print(sum(map(int, my_list)))
