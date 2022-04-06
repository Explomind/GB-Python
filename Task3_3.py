# Найти сумму отрицательных элементов в списке

new_list = [2, -56, 0, 32, -11, 98, -4]
sum_neg = 0
for item in new_list:
    if item < 0:
        sum_neg +=item
print('List: {1}\nSum of negative elements: {0}'.format(sum_neg, new_list))
