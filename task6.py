from itertools import count, cycle

for el in count(5):
    if el > 25:
        break
    else:
        print(el)


my_list = ['red', 'green', 'yellow', 'blue']
elem = 0
for el in cycle(my_list):
    if elem > 11:
        break
    print(el)
    elem += 1
