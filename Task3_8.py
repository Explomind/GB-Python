# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def series(number):
    result = [1]
    for i in range(1, number):
        result.append(result[i - 1] * -3)
    return result


number = int(input('Input number: '))
print(series(number))
