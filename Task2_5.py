# # n человек, пронумерованных числами от 1 до n, стоят в кругу. Они начинают считаться, каждый k-й по счету человек
# # выбывает из круга, после чего счет продолжается со следующего за ним человека. Напишите программу, определяющую номер
# # человека, который останется в кругу последним.

def count_circle(amount, drop):
    circle = list(range(1, amount + 1))
    print(circle)
    count = 0
    i = 0
    length = len(circle)
    while length > 1:
        if i == len(circle):
            i = 0
        if circle[i] != 0:
            count += 1
            if count % drop == 0:
                circle[i] = 0
                length -= 1
        i += 1
    last = 0
    for item in circle:
        last += item
    return last


amount_in_circle = int(input('Input amount of people in circle: '))
drop_number = int(input('Input number of man who is to drop from circle: '))
print('Last man: {0}'.format(count_circle(amount_in_circle, drop_number)))
