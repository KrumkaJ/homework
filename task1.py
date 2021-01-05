from sys import argv

script_name, working_out, rate, prize = argv

print('Выработка в часах: ', working_out)
print('Ставка в часах: ', rate)
print('Премия: ', prize)

result = (int(working_out) * int(rate) + int(prize))
print(f'Заработная плата: {result}')
