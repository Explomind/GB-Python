# Найти максимальное из 5 чисел

numbers = []
for i in range(5):
    numbers.append(int(input(f'Input {i+1} number = ')))
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number
print('Maximum number = ', max_number)
