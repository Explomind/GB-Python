# Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

def math_expr_str_to_list(str_expr):
    signs = ['+', '-', '/', '*']
    expr_list = []
    start = 0
    tmp_num = ''
    if str_expr[0] == '-':
        start = 1
        tmp_num += str_expr[0]
    for i in range(start, len(str_expr)):
        if str_expr[i] in signs:
            expr_list.append(int(tmp_num))
            tmp_num = ''
            expr_list.append(str_expr[i])
        else:
            tmp_num += str_expr[i]
    expr_list.append(int(tmp_num))
    return expr_list


def division(expr_list):
    start = 1
    pos_div = 0
    expr_end = len(expr_list)
    while start < expr_end and pos_div != -1:
        try:
            pos_div = expr_list.index('/', start)
            result = expr_list[pos_div - 1] / expr_list[pos_div + 1]
            expr_list.insert(pos_div - 1, result)
            for i in range(3):
                expr_list.pop(pos_div)
            start = pos_div
            expr_end -= 2
        except ValueError:
            pos_div = -1
    return expr_list


def multi(expr_list):
    start = 1
    pos_multi = 0
    expr_end = len(expr_list)
    while start < expr_end and pos_multi != -1:
        try:
            pos_multi = expr_list.index('*', start)
            result = expr_list[pos_multi - 1] * expr_list[pos_multi + 1]
            expr_list.insert(pos_multi - 1, result)
            for i in range(3):
                expr_list.pop(pos_multi)
            start = pos_multi
            expr_end -= 2
        except ValueError:
            pos_multi = -1
    return expr_list


def sum(expr_list):
    result = expr_list[0]
    for i in range(len(expr_list) - 1):
        if expr_list[i] == '+':
            result += expr_list[i + 1]
        elif expr_list[i] == '-':
            result -= expr_list[i + 1]
    return result


def calc(str_expr):
    expr_list = math_expr_str_to_list(str_expr)
    result = multi(expr_list)
    result = division(result)
    result = sum(result)
    return result


def calc_with_par(str_expr):
    if str_expr.find('(') != -1:
        start = str_expr.find('(') + 1
        end = str_expr.find(')')
        expr_in_pars = str_expr[start:end]
        str_expr = str_expr[:start - 1] + str(calc(expr_in_pars)) + str_expr[end + 1:]
    return calc(str_expr)


math_expression = '-20 / 4 + 4 * 6 - 10'
print('{} = {}'.format(math_expression, calc(math_expression)))
math_expression = '-20 / 4 + 4 * (18 - 10) - 3'
print('{} = {}'.format(math_expression, calc_with_par(math_expression)))
