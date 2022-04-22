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

# print(common_fraction_input())
