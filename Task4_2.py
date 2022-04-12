# Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

def index_second(str_list, seek_string):
    result = -1
    count = 0
    i = 0
    for i in range(len(str_list)):
        if str_list[i] == seek_string:
            count += 1
        if count == 2:
            result = i
            break
    return result


str_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
seek_str = 'qwe'
print('List:\t{0}\nSecond index:\t{1}'.format(str_list, index_second(str_list, seek_str)))
str_list = ["123", "234", 123, "567"]
seek_str = '123'
print('List:\t{0}\nSecond index:\t{1}'.format(str_list, index_second(str_list, seek_str)))
str_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
seek_str = 'йцу'
print('List:\t{0}\nSecond index:\t{1}'.format(str_list, index_second(str_list, seek_str)))
