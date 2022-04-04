# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов.
# При смешивании двух основных цветов получается вторичный цвет:
#     • если смешать красный и синий, то получится фиолетовый;
#     • если смешать красный и желтый, то получится оранжевый;
#     • если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит
# что-нибудь помимо названий «красный», «синий» или «желтый», то программа должна вывести сообщение об ошибке.
# В противном случае программа должна вывести название вторичного цвета, который получится в результате


def color_mix(color_1, color_2):
    colors_dict = {'red': 1, 'blue': 10, 'yellow': 100, 11: 'purple', 101: 'orange', 110: 'green'}
    if color_1 not in colors_dict.keys() or color_2 not in colors_dict.keys():
        print('Error! You should input one of main colors: red, blue or yellow')
    elif color_1 == color_2:
        print('Mixed color: {0}'.format(color_1))
    else:
        # print('Ok')
        key = colors_dict[color_1] + colors_dict[color_2]
        # print('color_1 key: {0}, color_2 key: {1}'.format(colors_dict.keys(color_1), colors_dict.keys(color_2)))
        print('Mixed color: {0}'.format(colors_dict[key]))


color_1 = input('Input the first color (red, blue or yellow): ')
color_2 = input('Input the second color (red, blue or yellow): ')
color_mix(color_1, color_2)
