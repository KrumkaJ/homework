import json

profit_firm = {}
av_profit = {}
profit = 0
average_profit = 0
i = 0

with open('seventh.txt', 'r', encoding='utf-8') as my_f:
    for line in my_f:
        name, form, proceeds, costs = line.split()
        profit_firm[name] = int(proceeds) - int(costs)
        if profit_firm.setdefault(name) >= 0:
            profit = profit + profit_firm.setdefault(name)
            i += 1
    if i != 0:
        average_profit = profit / i
    av_profit = {'Средняя прибыль': round(average_profit)}
    my_list = [profit_firm, av_profit]
    print(f'Прибыль и убытки фирм - {my_list}')

with open('seventh.json', 'w') as my_json:
    json.dump(my_list, my_json)
