def input_green():
    green_letters = input('Введите все "зеленые" буквы (формат: _а__б): ')
    return green_letters


def input_yellow():
    yellow_letters = input('Введите все "желтые" буквы с учетом новых позиций (формат: _а_б_): ')
    return yellow_letters


def input_grey(grey_letters=''):
    grey_letters += input('Введите новые "серые" буквы в строку без пробелов (формат: абв): ')
    return grey_letters


def menu():
    menu_items = '123456'
    instruction = ['1 - ввести "зеленые" буквы',
                   '2 - ввести "желтые" буквы',
                   '3 - ввести "серые" буквы',
                   '4 - показать слова',
                   '5 - показать случайное слово',
                   '6 - выход']
    for each in instruction:
        print(each)
    while True:
        choice = input('Что сделать: ')
        if choice in menu_items:
            return choice
        else:
            print('Нет такого пункта!')


def show_words(data, amount):
    start = 0
    end = amount
    while True:
        line = ''
        for i in range(start, end):
            if i == len(data):
                print(line)
                return
            line += data[i] + '\t'
        print(line)
        start = end
        end += amount
