# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

def strings_compare(string_1, string_2):
    # if len(string_1) > len(string_2):
    #     tmp = string_1
    #     string_1 = string_2
    #     string_2 = tmp
    j = 0
    count = 0
    while j < len(string_2):
        if string_1[0] == string_2[j]:
            tmp = string_2[j:j + len(string_1)]
            if string_1 == tmp:
                count += 1
                j += len(string_1)
            else:
                j += 1
        else:
            j += 1
    return count

string_1 = input('Input the first string: ')
string_2 = input('Input the second string: ')
if len(string_1) > len(string_2):
    tmp = string_1
    string_1 = string_2
    string_2 = tmp
print('The number of occurences of one string in another: {0}'.format(strings_compare(string_1, string_2)))
print('Check: {0}'.format(string_2.count(string_1)))
