# Написать программу преобразования десятичного числа в двоичное

def dec_to_byte(dec_number):
    result = ''
    while dec_number > 0:
        result += str(dec_number % 2)
        dec_number = dec_number // 2
    return result[::-1]

number = int(input('Input positive number: '))
print('In binary system: {0}'.format(dec_to_byte(number)))
