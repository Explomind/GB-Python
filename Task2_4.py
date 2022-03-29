# Дано пятизначное или шестизначное натуральное число.
# Напишите программу, которая изменит порядок его последних пяти цифр на обратный.

def change_order(number, last_digits_qnt):
    if len(number) >= last_digits_qnt + 1:
        last_digits = number[:len(number) - last_digits_qnt - 1:-1]
        result_int = int(number[0:len(number) - last_digits_qnt] + last_digits)
    else:
        result_int = int(number[::-1])
    return result_int


int_number = input('Input 5- or 6-digit number: ')
qnt_last_digits = int(input('Input amount of digits to change: '))
print(change_order(int_number, qnt_last_digits))
