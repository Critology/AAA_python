import csv


def reading_file_in_dict(file_name='HW_2/Corp_Summary.csv') -> dict:
    """Считываем csv в словарь"""
    with open(file_name, 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        my_list = []
        for line in reader:
            my_list.append(line[0].split(';'))
        my_dict = {}
        keys = my_list[0]
        for elem in keys:
            my_dict[elem] = []
        for row in my_list[1:]:
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
                '"Вилка" зарплат': [10**10, 0], # сравнивать с первой зарплатой
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


def writing_file_from_dict(file_name='HW_2/Corp_Summary.csv') -> None:
    """Записываем наш словарь в csv"""
    my_dict = departments_summary()
    dict_in_list = []
    my_list_1 = []
    for el in my_dict:
        my_list_1.append(el)
    dict_in_list.append(my_list_1)
    for elem in my_dict:
        my_list_2 = []
        for val in my_dict[elem]:
            my_list_2.append(val+': '+str(my_dict[elem][val]))
        dict_in_list.append(my_list_2)
    print(dict_in_list)
    with open('HW_2/Department_Summary.csv', 'w', encoding='utf-8') as f:
        w = csv.writer(f, dict_in_list)
        w.writerow(dict_in_list[0])  # в строку
        w.writerows(dict_in_list[1:])


def choice_option():
    options = {
            '1': 'Вывести иерархию команд',
            '2': 'Вывести сводный отчёт по департаментам',
            '3': 'Сохранить сводный отчёт',
            '4': 'Выйти'
                }
    while True:
        print('Выберите: ')
        for k, v in options.items():
            print(k, v)
        opt = input()
        if opt == '1':
            print(teams_in_departments())
        elif opt == '2':
            print(departments_summary())
        elif opt == '3':
            writing_file_from_dict()
        else:
            return


if __name__ == '__main__':
    choice_option()
