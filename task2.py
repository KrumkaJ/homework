numbers = int(input('Введите количество элементов в списке: '))
i = 0
members = []
element = 0

while i < numbers:
    members.append(input(f'Введите элемент списка '))
    i += 1
print(list(members))

for index in range(int(len(members)/2)):
    members[element], members[element + 1] = members[element + 1], members[element]
    element += 2
print(members)
