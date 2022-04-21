# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

def unique_items(any_list):
    tmp_set = set(any_list)
    result = []
    for each in tmp_set:
        count = 0
        for i in range(len(any_list)):
            if each == any_list[i]:
                count += 1
        if count == 1:
            result.append(each)
    return result


any_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(unique_items(any_list))
