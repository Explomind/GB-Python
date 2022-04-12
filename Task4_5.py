# Найти НОК двух чисел

def GCD(number_1, number_2):
    if number_1 % number_2 == 0:
        return number_2
    elif number_2 % number_1 == 0:
        return number_1
    elif number_1 > number_2:
        return GCD((number_1 % number_2), number_2)
    else:
        return GCD(number_1, (number_2 % number_1))

def LCM(number_1, number_2):
    return (number_1 * number_2) // GCD(number_1, number_2)

A = int(input('Input the first number: '))
B = int(input('Input the second number: '))
print('Greatest common divisor = {0}'.format(GCD(A, B)))
print('Least common multiple = {0}'.format(LCM(A, B)))
