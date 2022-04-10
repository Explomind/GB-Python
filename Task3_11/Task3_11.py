# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt(по желанию) в одной строке одно число

def rand_int_list(number):
    from random import randint
    result = []
    for item in range(number):
        result.append(randint(-number, number))
    return result


def multiply(int_list):
    path = 'file.txt'
    data = open(path, 'r')
    result = 1
    for pos in data:
        result *= int_list[int(pos)]
    return result


# number = int(input('Input N: '))
# print(rand_int_list(10))
int_list = rand_int_list(5)
print(int_list)
print('Product of numbers = {0}'.format(multiply(int_list)))
