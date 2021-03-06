# В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найти его и добавить в файл.

def seek_lost(string):
    # int_list = [int(item) for item in string.split()]
    int_list = list(map(int, string.split()))
    print(int_list)
    for i in range(1, len(int_list)):
        if int_list[i] - 1 != int_list[i - 1]:
            int_list.append(int_list[i] - 1)
    int_list.sort()
    result = ' '.join(map(str, int_list))
    return result


with open('Task5_4.txt', 'r') as file:
    old_string = str(file.read())
new_string = seek_lost(old_string)
print(new_string)
with open('Task5_4.txt', 'w') as data:
    data.write(new_string)
