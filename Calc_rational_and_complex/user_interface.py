def common_fraction_input():
    while True:
        str_number = input('Input common fraction (e.g. 5/7): ')
        try:
            slash_pos = str_number.find('/')
            if slash_pos == -1:
                int(str_number)
                break
            else:
                int(str_number[:slash_pos])
                if int(str_number[slash_pos + 1:]) == 0:
                    print('Incorrect input!')
                else:
                    break
        except ValueError:
            print('Incorrect input!')
    return str_number


def operation_input():
    while True:
        operation = input('Input arithmetic operation (+, -, *, /): ')
        if operation in '+-*/':
            break
        else:
            print('Incorrect input!')
    return operation


def menu():
    descript = ['This is calculator to operate with rational and complex numbers.',
                'Possible actions: sum "+", subtraction "-", multiplication "*", division "/"']
    print(*descript, sep='\n')
    menu_items = '12'
    menu_text = 'Choose type of numbers: {0} - rational, {1} - complex\n' \
        .format(menu_items[0], menu_items[1])
    while True:
        num_type = input(menu_text)
        if num_type in menu_items:
            return num_type
        else:
            print('Incorrect input!')
