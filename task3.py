# # список
season_list = ['winter', 'spring', 'summer', 'autumn']

month = int(input('Введите номер месяца '))

if month == 1 or month == 2 or month == 12:
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])
else:
    print('Error')

# словарь
season_dict = {'season_1': 'winter', 'season_2': 'spring', 'season_3': 'summer', 'season_4': 'autumn'}

month = int(input('Введите номер месяца '))

if month == 1 or month == 2 or month == 12:
    print(season_dict.get('season_1'))
elif month == 3 or month == 4 or month == 5:
    print(season_dict.get('season_2'))
elif month == 6 or month == 7 or month == 8:
    print(season_dict.get('season_3'))
elif month == 9 or month == 10 or month == 11:
    print(season_dict.get('season_4'))
else:
    print('Error')