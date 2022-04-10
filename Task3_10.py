# Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

def sum_series(n):
    series_list = [(1 + int('1' + str(i))) * i for i in range(1, n + 1)]
    print(*series_list)
    result = sum(series_list)
    return result

number = int(input('Input number: '))
print('Sum of elements = {0}'.format(sum_series(number)))
