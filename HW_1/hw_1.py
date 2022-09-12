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
    print(
        'Утка добирается до места назначения, садится за барную стойку '
        'и берет кружечку жидкого золота🍺'
    )
    answer = ''
    drinking = True
    num_beers = 2
    while drinking:
        print(
            f'Налить {num_beers} кружку? '
            'Выберите: да/нет'
        )
        answer = input()
        if answer == 'нет':
            drinking = False
            return print('Утка хорошо провела время и ушла спать домой.')
        elif num_beers > 5:
            return print(
                'Утка начала буянить, '
                'ей вызвали такси и указали на дверь.'
            )
        elif num_beers > 3:
            print('Хватит спаивать утку' + '😡' * (num_beers - 3))
            num_beers += 1
        else:
            num_beers += 1


def step2_no_umbrella():
    return print('Пошел дождь, утка не хочет мокнуть и возвращается домой ☹')


if __name__ == '__main__':
    step1()
