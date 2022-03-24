# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

print('Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30')
number = int(input('Input number: '))
print((number % 10 == 0 or number % 15 == 0) and number % 30 != 0)
