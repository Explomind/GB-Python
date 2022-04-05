# Заданы две клетки шахматной доски. Напишите программу, которая определяет имеют ли указанные клетки один цвет или нет.
# Если они покрашены в один цвет, то выведите слово «YES», а если в разные цвета — то «NO».

def check_coords(square_1, square_2):
    letters_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
    square_1_color = 'Error square 1'
    square_2_color = 'Error square 2'
    if len(square_1) == 2 and len(square_2) == 2:
        if square_1[0] in letters_dict.keys() and square_2[0] in letters_dict.keys():
            square_1_x = letters_dict[square_1[0]]
            square_1_y = int(square_1[1])
            square_2_x = letters_dict[square_2[0]]
            square_2_y = int(square_2[1])
            if square_1_y in range(1, 9) and square_2_y in range(1, 9):
                if (square_1_x % 2) == (square_1_y % 2):
                    square_1_color = 'black'
                else:
                    square_1_color = 'white'
                if (square_2_x % 2) == (square_2_y % 2):
                    square_2_color = 'black'
                else:
                    square_2_color = 'white'
    print('{2}: {0}\n{3}: {1}'.format(square_1_color, square_2_color, square_1, square_2))
    return square_1_color, square_2_color

def check_colors(color_1, color_2):
    if color_1 == color_2:
        print('YES')
    else:
        print('NO')

square_1 = input('Input cell 1 (a1..h8): ')
square_2 = input('Input cell 2 (a1..h8): ')
color_sq_1, color_sq_2 = check_coords(square_1, square_2)
check_colors(color_sq_1, color_sq_2)
