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


def complex_num_input():
    while True:
        str_number = input('Input complex number (e.g. 2+3j): ')
        try:
            if 'j' not in str_number:
                return int(str_number)
            else:
                sign_pos = str_number.find('+')
                if sign_pos != -1:
                    real_part = int(str_number[:sign_pos])
                    imag_part = int(str_number[sign_pos + 1:-1])
                else:
                    sign_pos = str_number.rfind('-')
                    if sign_pos in range(-1, 1):
                        real_part = 0
                        imag_part = int(str_number[:-1])
                    else:
                        real_part = int(str_number[:sign_pos])
                        imag_part = int(str_number[sign_pos:-1])
                return complex(real_part, imag_part)
        except ValueError:
            print('Incorrect input!')


def operation_input():
    while True:
        operation = input('Input arithmetic operation (+, -, *, /): ')
        if operation in '+-*/':
            return operation
        else:
            print('Incorrect input!')


def menu():
    descript = ['Calculator to operate with rational and complex numbers.',
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
