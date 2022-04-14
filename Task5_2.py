# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k. *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def rand_polynomial(upper_degree):
    if upper_degree < 1:
        return 'Error!'
    from random import randint
    coefs = [randint(0, 100) for coefs in range(upper_degree + 1)]
    # print(coefs)
    result = ' = 0'
    for degree in range(upper_degree + 1):
        if coefs[degree] != 0:
            if degree == 0:
                result = str(coefs[degree]) + result
            elif degree == 1:
                result = str(coefs[degree]) + '*x + ' + result
            else:
                result = str(coefs[degree]) + '*x^' + str(degree) + ' + ' + result
    return result


upper_degree = int(input('Input upper degree of a polynomial (>0): '))
polynomial_str = rand_polynomial(upper_degree)
print(polynomial_str)
with open('Task5_2.txt', 'a') as data:
    data.write(polynomial_str + '\n')

