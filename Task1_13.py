# Сложите цифры целого числа.

number = int(input('Input number: '))
if number < 0:
    number *= -1
sum_digits = 0
while number > 0:
    sum_digits += number % 10
    number = number // 10
print(f'Sum of digits = {sum_digits}')
