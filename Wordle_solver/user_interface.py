def input_green():
    green_letters = input('Введите "зеленые" буквы (формат: _а__б): ')
    return green_letters


def input_yellow():
    yellow_letters = input('Введите все "желтые" буквы с учетом новых позиций (формат: _а_б_): ')
    return yellow_letters


def input_grey(grey_letters=''):
    grey_letters += input('Введите новые "серые" буквы: ')
    return grey_letters


def menu():
    menu_items = '12345'
    instruction = ['1 - ввести "зеленые" буквы',
                   '2 - ввести "желтые" буквы',
                   '3 - ввести "серые" буквы',
                   '4 - показать слова',
                   '5 - выход']
    for each in instruction:
        print(each)
    while True:
        choice = input('Что сделать: ')
        if choice in menu_items:
            return choice
        else:
            print('Нет такого пункта!')
