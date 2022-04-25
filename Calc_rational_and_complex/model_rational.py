# операции с обыкновенными дробями
from math import gcd


def str_to_common_fraction(number):  # разложение строкового представления дроби на числитель и знаменатель
    slash_pos = number.find('/')
    if slash_pos != -1:
        numerator = int(number[:slash_pos])
        denominator = int(number[slash_pos + 1:])
    else:
        numerator = int(number)
        denominator = 1
    return (numerator, denominator)


def calculation(number_1, number_2, operation):  # вычисления
    num_1_numer, num_1_denom = str_to_common_fraction(number_1)
    num_2_numer, num_2_denom = str_to_common_fraction(number_2)
    numer_1_denom_2 = num_1_numer * num_2_denom
    numer_2_denom_1 = num_2_numer * num_1_denom
    denom_1_denom_2 = num_1_denom * num_2_denom
    if operation == '+':
        result = str(numer_1_denom_2 + numer_2_denom_1) + '/' + str(denom_1_denom_2)
    elif operation == '-':
        result = str(numer_1_denom_2 - numer_2_denom_1) + '/' + str(denom_1_denom_2)
    elif operation == '*':
        result = str(num_1_numer * num_2_numer) + '/' + str(denom_1_denom_2)
    else:
        result = str(numer_1_denom_2) + '/' + str(numer_2_denom_1)
    return fraction_simpl(result)


def fraction_simpl(com_fract):  # упрощение дроби
    numer, denom = str_to_common_fraction(com_fract)
    result_numer = numer // gcd(numer, denom)
    denom //= gcd(numer, denom)
    if result_numer == denom:
        return '1'
    elif result_numer > denom:
        result = str(result_numer // denom) + ' ' + str(result_numer % denom)
    else:
        result = str(result_numer)
    return result + '/' + str(denom)
