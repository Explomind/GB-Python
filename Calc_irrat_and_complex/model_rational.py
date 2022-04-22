# операции с обыкновенными дробями
from math import gcd


# def lcm(number_1, number_2):   # наименьшее общее кратное
#     return (number_1 * number_2) // gcd(number_1, number_2)


def mod_common_fraction(number):  # разложение строкового представления дроби на числитель и знаменатель
    slash_pos = number.find('/')
    if slash_pos != -1:
        numerator = int(number[:slash_pos])
        denominator = int(number[slash_pos + 1:])
    else:
        numerator = int(number)
        denominator = 1
    return (numerator, denominator)


def init(number_1, number_2):  # инициация глобальных переменных числителей и знаменателей дробей
    global num_1_numer
    global num_1_denom
    global num_2_numer
    global num_2_denom
    num_1_numer, num_1_denom = mod_common_fraction(number_1)
    num_2_numer, num_2_denom = mod_common_fraction(number_2)


def sum_fract():  # сложение
    return str(num_1_numer * num_2_denom + num_2_numer * num_1_denom) + '/' + str(num_1_denom * num_2_denom)


def subtract():  # вычитание
    return str(num_1_numer * num_2_denom - num_2_numer * num_1_denom) + '/' + str(num_1_denom * num_2_denom)


def multi():  # умножение
    return str(num_1_numer * num_2_numer) + '/' + str(num_1_denom * num_2_denom)


def division():  # деление
    return str(num_1_numer * num_2_denom) + '/' + str(num_2_numer * num_1_denom)


def fraction_simpl(com_fract):  # упрощение дроби
    numer, denom = mod_common_fraction(com_fract)
    result_numer = numer // gcd(numer, denom)
    denom //= gcd(numer, denom)
    if result_numer == denom:
        return '1'
    elif result_numer > denom:
        result = str(result_numer // denom) + ' ' + str(result_numer % denom)
    else:
        result = str(result_numer)
    return result + '/' + str(denom)
