# Дан словарь,найти сумму всех ключей и значений словаря.

dict = {1: 3, 5: 5, 6: 4, 7: 6}
sum_keys = 0
sum_values = 0
for key in dict:
    sum_keys += key
    sum_values += dict[key]
print(dict)
print('First method:\nSum of keys = {0}\nSum of values = {1}'.format(sum_keys, sum_values))
print()
# print(*dict.values())
# print(*dict.keys())
sum_keys = 0
sum_values = 0
for key in dict.keys():
    sum_keys += key
for value in dict.values():
    sum_values += value
print('Second method:\nSum of keys = {0}\nSum of values = {1}'.format(sum_keys, sum_values))
print()
sum_keys = 0
sum_values = 0
for key, value in dict.items():
    sum_keys += key
    sum_values += value
print('Third method:\nSum of keys = {0}\nSum of values = {1}'.format(sum_keys, sum_values))

