# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-------------')


def take_input(player_token):
    while True:
        turn_pos = int(input('Куда поставить {}: '.format(player_token)))
        if turn_pos in range(1, 10):
            if board[turn_pos - 1] in range(1, 10):
                board[turn_pos - 1] = player_token
                break
            else:
                print('The field is occupied! Choose another!')
        else:
            print('Invalid input!')


def check_win(board):
    win_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
    for item in win_list:
        if board[item[0] - 1] == board[item[1] - 1] == board[item[2] - 1]:
            return True
    return False


def main(board):
    print('----------------')
    print('Tic-tac-toe game')
    print('----------------')
    draw_board(board)
    win = False
    player_turn = 0
    while not win:
        if player_turn > 8:
            break
        if player_turn % 2:
            player_token = 'O'
        else:
            player_token = 'X'
        player_turn += 1
        take_input(player_token)
        draw_board(board)
        if player_turn > 4:
            win = check_win(board)
    if win:
        print('{} win!'.format(player_token))
    else:
        print('The game ended in a draw!')


board = list(range(1, 10))
main(board)
