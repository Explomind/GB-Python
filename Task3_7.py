# Определить, присутствует ли в заданном списке строк, некоторое число

def seek_number(str_list, number):
    str_number = str(number)
    for string in str_list:
        if str_number in string:
            return True
        else:
            continue
    return False


str_list = ['123', '55df', 's7ds4', '934']
print(*str_list)
number = int(input('Input number: '))
print(seek_number(str_list, number))
