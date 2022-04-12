# Найти сумму чисел списка стоящих на нечетной позиции

spisok = [2, 1, 54, 1, 0, 1, 3, 45]
sum_odd = 0
for i in range(1, len(spisok), 2):
    sum_odd += spisok[i]
print('List:\t{1}\nSum of items in odd positions: {0}'.format(sum_odd, spisok))
