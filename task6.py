import re

subjects_dict = {}
with open('sixth.txt', encoding='utf-8') as my_f:
    subjects = my_f.readlines()
    for line in subjects:
        my_line = line.split(':')
        subject = my_line[0]
        # ищем в строке цифры - одну или более, и складываем
        sum_lessons = sum([int(num) for num in (re.findall('\d+', my_line[1]))])
        subjects_dict[subject] = sum_lessons
print(subjects_dict)
