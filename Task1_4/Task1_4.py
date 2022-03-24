# Показать первую цифру дробной части числа

number = float(input('Input a fractional number: ')) * 10
if number < 0:
    number *= -1
remainder = int(number % 10)
print(f'The first digit after "," = {remainder}')
