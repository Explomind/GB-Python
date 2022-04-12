# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

def random_int(min, max):
    len_min = len(str(min))
    len_max = len(str(max))
    import time
    qnt = time.time_ns() % 10  # количество знаков в числе [0,9]
    if qnt < len_min:
        qnt = len_min
    if qnt > len_max:
        qnt = len_max
    while True:
        result = int(str(time.time_ns())[-qnt:])
        if result in range(min, max + 1):
            break
    return result


print(random_int(0, 100))
