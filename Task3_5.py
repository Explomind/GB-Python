# Подсчитать сумму цифр в вещественном числе.

def sum_digits(number):
    number = str(number)
    result = 0
    for char in number:
        if char != '-' and char != '.':
            result += int(char)
    return result

number = float(input('Input number: '))
print('Sum of digits = {0}'.format(sum_digits(number)))
