# При заданном целом числе n посчитайте n + nn + nnn.

n = int(input('Input number n = '))
result = 0
for i in range(1,4):
    result = result + n ** i
print(f'n + nn + nnn = {result}')
