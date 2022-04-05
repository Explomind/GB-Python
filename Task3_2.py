# Найти максимальный и минимальный элемент в списке чисел.

def min_item(list_min):
    min_value = list_min[0]
    for item in list_min:
        if item < min_value:
            min_value = item
    return min_value

def max_item(list_max):
    max_value = list_max[0]
    for item in list_max:
        if item > max_value:
            max_value = item
    return max_value

list_min_max = [1, 2, 10, 4242, 2442]
print('List: {2}\nMinimum value: {0}\nMaximum value: {1}'.format(min_item(list_min_max),
                                                                 max_item(list_min_max),
                                                                 list_min_max))
