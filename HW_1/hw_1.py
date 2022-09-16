def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    """Функция описывает случай когда утка взяла зонт и пошла выпть в бар"""
    print(
        'Утка добирается до места назначения, садится за барную стойку '
        'и берет кружечку жидкого золота🍺'
    )
    answer = ''
    num_beers = 2
    while True:
        print(
            f'Налить {num_beers} кружку? '
            'Выберите: да/нет'
        )
        answer = input()
        if answer == 'нет':
            return print('Утка хорошо провела время и ушла спать домой.')

        if num_beers > 2 and num_beers < 5:
            print('Хватит спаивать утку' + '😡' * (num_beers - 2))
            num_beers += 1
        else:
            num_beers += 1

        if num_beers > 5:
            return print(
                'Утка начала буянить, '
                'ей вызвали такси и указали на дверь.'
            )


def step2_no_umbrella():
    """Функция описывает случай когда утка не взяла зонт"""
    return print('Пошел дождь, утка не хочет мокнуть и возвращается домой ☹')


if __name__ == '__main__':
    step1()
