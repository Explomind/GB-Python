# Написать калькулятор с операциями: Умножение,деление, остаток от деления, вычитание, целочисленное деление.

def calc(number1, number2, sign):
    if sign == '+':
        return number1 + number2
    elif sign == '-':
        return number1 - number2
    elif sign == '*':
        return number1 * number2
    elif sign == '/':
        return number1 / number2
    elif sign == '%':
        return number1 % number2
    elif sign == '//':
        return number1 // number2
    else:
        print('This calc uses only: + - * / % //')


a = float(input('Input first number: '))
b = float(input('Input second number: '))
s = input('Input sign: ')
if b == 0 and (s == '/' or s == '%' or s == '//'):
    print("This calc can't divide by 0.")
else:
    print(calc(a, b, s))
