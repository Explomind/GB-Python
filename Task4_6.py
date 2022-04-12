# Составить список простых множителей натурального числа N

def simple_numbers(N):
    num_dict = {num: num for num in range(2, N + 1)}
    result = []
    for i in num_dict.keys():
        j = i ** 2
        while j <= N:
            num_dict[j] = 0
            j += i
        if num_dict[i] != 0:
            result.append(num_dict[i])
    return result


def simple_factors(number):
    simple_list = simple_numbers(int(number ** 0.5))
    result = []
    i = 0
    while number > 1:
        if i >= len(simple_list):
            simple_list.append(number)
        if number % simple_list[i] == 0:
            number = number // simple_list[i]
            result.append(simple_list[i])
        else:
            i += 1
    return result


number = int(input('Input number: '))
print('Prime factors of a number {0}:\n{1}'.format(number, simple_factors(number)))
