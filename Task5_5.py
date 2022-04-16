# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность
# и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#    [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

def long_list(int_list):
    result_list = []
    for i in range(len(int_list)):
        for j in range(i + 1, len(int_list)):
            tmp_list = [int_list[i]]
            tmp = int_list[i]
            for k in range(j, len(int_list)):
                if int_list[k] > tmp:
                    tmp = int_list[k]
                    tmp_list.append(tmp)
            if len(tmp_list) > len(result_list):
                result_list = tmp_list
    return result_list


list_1 = [1, 5, 2, 3, 4, 6, 1, 7]
list_2 = [5, 2, 3, 4, 6, 1, 7]
print(long_list(list_1))
print(long_list(list_2))
