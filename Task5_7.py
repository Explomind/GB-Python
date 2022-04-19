# Помните игру с конфетами из модуля "Математика и Информатика"? Создайте такую игру для игры человек против человека
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

def player_to_player(first_turn, candies=121):
    print('На столе конфет: {}'.format(candies))
    turn = first_turn
    player_turn = 0
    max_turn = 28
    while candies > 0:
        if max_turn > candies:
            max_turn = candies
        while player_turn not in range(1, max_turn + 1):
            print('Можно забрать от 1 до {} конфет.'.format(max_turn))
            player_turn = int(input('Ход игрока {}: '.format(turn % 2 + 1)))
        candies -= player_turn
        player_turn = 0
        turn += 1
        print('Осталось конфет: {}'.format(candies))
        if turn % 2:
            winner = 1
        else:
            winner = 2
    return winner


def player_to_comp(difficulty, first_turn, candies=121):
    from random import randint
    print('На столе конфет: {}'.format(candies))
    turn = first_turn
    player_turn = 0
    max_turn = 28
    while candies > 0:
        if max_turn > candies:
            max_turn = candies
        if not turn % 2:
            while player_turn not in range(1, max_turn + 1):
                print('Можно забрать от 1 до {} конфет.'.format(max_turn))
                player_turn = int(input('Ход игрока: '))
            winner = 1
        else:
            if candies > 28:
                ideal_turn = candies % 29
                if ideal_turn <= difficulty:
                    player_turn = randint(1, difficulty * 2)
                elif ideal_turn >= max_turn - difficulty:
                    player_turn = randint(max_turn - difficulty * 2, max_turn)
                else:
                    player_turn = randint(ideal_turn - difficulty, ideal_turn + difficulty)
            else:
                player_turn = candies
            print('Компьютер забрал конфет: {}'.format(player_turn))
            winner = 2
        candies -= player_turn
        player_turn = 0
        turn += 1
        print('Осталось конфет: {}'.format(candies))
    return winner

def toss():
    from random import randint
    return randint(0, 1)

def start_game():
    print('1 - 1 игрок\t\t2 - 2 игрока')
    option = int(input('Выберите тип игры: '))
    first_turn = toss()
    if option == 1:
        difficulty = int(input('Выберите сложность от 1 до 12 (чем меньше число, тем сложнее):\n'))
        if difficulty < 1:
            difficulty = 1
        elif difficulty > 12:
            difficulty = 12
        winner = player_to_comp(difficulty, first_turn)
        if winner == 1:
            print('Вы выиграли!')
        else:
            print('Вы проиграли!')
    elif option == 2:
        winner = player_to_player(first_turn)
        print('Победил игрок {}!'.format(winner))
    else:
        print('Ошибка ввода!')


with open('Task5_7.txt', 'r') as file:
    while True:
        rules_text = file.readline()
        if not rules_text:
            break
        print(rules_text.strip())
print()
start_game()
