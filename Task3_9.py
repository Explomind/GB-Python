# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def dict_series(n):
    return {item: 3 * item + 1 for item in range(1, n + 1)}


number = int(input('Input number: '))
print(dict_series(number))
