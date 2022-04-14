# Даны два файла в каждом из которых находится запись многочлена. Сформировать файл содержащий сумму многочленов.

def poly_str_coefs(path):
    with open(path, 'r') as file:
        polynom = str(file.read())[:-3]
    x_pos = polynom.find('x')
    degree = int(polynom[x_pos + 2])
    coefs_dict = {key: 0 for key in range(degree + 1)}
    tmp_list = polynom.split('+')
    for i in range(len(tmp_list)):
        tmp_list[i] = tmp_list[i].strip()
    for string in tmp_list:
        if string.isdigit():
            coefs_dict[0] = int(string)
        elif string[-1] == 'x':
            coefs_dict[1] = int(string[:-2])
        else:
            degree_key = int(string[-1])
            coefs_dict[degree_key] = int(string[:-4])
    return coefs_dict


def dict_sum(dict_1, dict_2):
    if len(dict_1) > len(dict_2):
        new_dict = dict_1.copy()
        for i in range(len(dict_2)):
            new_dict[i] += dict_2[i]
    elif len(dict_2) > len(dict_1):
        new_dict = dict_2.copy()
        for i in range(len(dict_1)):
            new_dict[i] += dict_1[i]
    else:
        new_dict = {i: dict_1[i] + dict_2[i] for i in range(len(dict_1))}
    return new_dict


def polynomial(coefs_dict):
    result = ' = 0'
    for degree in coefs_dict.keys():
        if degree == 0:
            result = str(coefs_dict[degree]) + result
        elif degree == 1:
            result = str(coefs_dict[degree]) + '*x + ' + result
        else:
            result = str(coefs_dict[degree]) + '*x^' + str(degree) + ' + ' + result
    return result


coefs_1 = poly_str_coefs('Task5_3(1).txt')
coefs_2 = poly_str_coefs('Task5_3(2).txt')
new_coefs = dict_sum(coefs_1, coefs_2)
new_polynom = polynomial(new_coefs)
print(new_polynom)
with open('Task5_3(result).txt', 'a') as data:
    data.write(new_polynom + '\n')
