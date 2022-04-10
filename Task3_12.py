# Реализовать алгоритм перемешивания списка.

def shuffle_list(int_list):
    shuffled_list = []
    from random import randint
    for i in range(len(int_list)):
        while True:
            index_tmp = randint(0, len(int_list) - 1)
            if int_list[index_tmp] not in shuffled_list:
                shuffled_list.append(int_list[index_tmp])
                break
    return shuffled_list


int_list = [1, 6, 95, 0, -8, 34]
print('First list:\t{0}\nShuffled list:\t{1}'.format(int_list, shuffle_list(int_list)))
