# На вход программе подается натуральное число n. Напишите программу, которая для каждого из чисел
# от 0 до n (включительно) выводит фразу: «Квадрат числа [число] равен [число]» (без кавычек).

def square_n(number):
    for num in range(number+1):
        print('Square number {0} = {1}'.format(num, num ** 2))


number = int(input('Input number: '))
square_n(number)
