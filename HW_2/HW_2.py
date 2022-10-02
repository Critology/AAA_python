import csv


def reading_file_in_dict(file_name='HW_2/Corp_Summary.csv') -> dict:
    """Считываем csv в словарь"""
    f = open(file_name, 'r', encoding='utf8')
    reader = csv.reader(f)
    my_list = []
    for line in reader:
        my_list.append(line[0].split(';'))
    my_dict = {}
    keys = my_list[0]
    my_list.pop(0)
    for elem in keys:
        my_dict[elem] = []
    for row in my_list:
        for i, elem in enumerate(keys):
            my_dict[elem].append(row[i])
    return my_dict


def teams_in_departments(file_name='HW_2/Corp_Summary.csv') -> dict:
    """Выводим список команд по каждому департаменту"""
    my_dict = reading_file_in_dict(file_name)
    dict_deps = {}
    for dep in my_dict['Департамент']:
        if dict_deps.get(dep) is None:
            dict_deps[dep] = []
    for key_dep in dict_deps.keys():
        for i, elem in enumerate(my_dict['Отдел']):
            if my_dict['Департамент'][i] == key_dep \
                        and elem not in dict_deps[key_dep]:
                dict_deps[key_dep].append(elem)
    return dict_deps


def departments_summary(file_name='HW_2/Corp_Summary.csv') -> dict:
    """Пишем сводник по департаментам в виде словаря"""
    my_dict = reading_file_in_dict(file_name)
    dict_deps = {}
    for dep in my_dict['Департамент']:
        if dict_deps.get(dep) is None:
            dict_deps[dep] = {
                'Численность': 0,
                '"Вилка" зарплат': [10**10, 0],
                'Средняя зарплата': [0, 0]
            }
    for key_dep in dict_deps.keys():
        for i, elem in enumerate(my_dict['Отдел']):
            if my_dict['Департамент'][i] == key_dep and elem not in dict_deps[key_dep]:
                dict_deps[key_dep]['Численность'] += 1
                if dict_deps[key_dep]['"Вилка" зарплат'][0] > int(my_dict['Оклад'][i]):
                    dict_deps[key_dep]['"Вилка" зарплат'][0] = int(my_dict['Оклад'][i])
                if dict_deps[key_dep]['"Вилка" зарплат'][1] < int(my_dict['Оклад'][i]):
                    dict_deps[key_dep]['"Вилка" зарплат'][1] = int(my_dict['Оклад'][i])
                dict_deps[key_dep]['Средняя зарплата'][0] += int(my_dict['Оклад'][i])
                dict_deps[key_dep]['Средняя зарплата'][1] \
                    = dict_deps[key_dep]['Средняя зарплата'][0] / dict_deps[key_dep]['Численность']
        dict_deps[key_dep]['Средняя зарплата'] = round(dict_deps[key_dep]['Средняя зарплата'][1])
    return dict_deps


def writing_file_from_dict(file_name='HW_2/Corp_Summary.csv'):
    """Записываем наш словарь в csv"""
    my_dict = departments_summary()
    with open('HW_2/Department_Summary.csv', 'w', encoding='utf-8') as f:
        w = csv.DictWriter(f, my_dict.keys())
        w.writeheader()
        w.writerow(my_dict)


print(departments_summary())
writing_file_from_dict()
