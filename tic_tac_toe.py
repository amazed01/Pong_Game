# https://github.com/Pierian-Data/Complete-Python-3-Bootcamp

from random import randint


def display_board(board):
    print(' ', '|', ' ', '|', ' ')
    print(board[7], '|', board[8], '|', board[9])
    print('_', '|', '_', '|', '_')
    print(' ', '|', ' ', '|', ' ')
    print(board[4], '|', board[5], '|', board[6])
    print('_', '|', '_', '|', '_')
    print(' ', '|', ' ', '|', ' ')
    print(board[1], '|', board[2], '|', board[3])
    print(' ', '|', ' ', '|', ' ')


def decide_player(player1, player2):
    player1 = input('Player 1: Choose "X" or "O"\t\t')
    print(player1)
    if player1.lower() == 'x':
        player1 = 'X'
        player2 = 'O'
        return 'X', 'O'
    elif player1.lower() == 'o':
        player2 = 'X'
        player1 = 'O'
        return 'O', 'X'
    else:
        return decide_player(None,None)


def result(board):
    r1, r2, r3 = board[7:10], board[4:7], board[1:4]
    c1, c2, c3 = [board[7], board[4], board[1]], [board[8], board[5], board[2]], [board[9], board[6], board[3]]
    d1, d2 = [board[7], board[5], board[3]], [board[9], board[5], board[1]]
    s = [r1, r2, r3, c1, c2, c3, d1, d2]

    if ['X'] * 3 in s:
        return True, 'X'
    elif ['O'] * 3 in s:
        return True, 'O'
    elif ' ' not in board:
        return True, 'Tied'
    else:
        return False, 'NO WINNER YET'


def play(i, turn, board, key, move):
    print(turn[i], 'make your move......')
    display_board(board)
    while True:
        mark = input()
        try:
            mark = int(mark)
            if mark not in range(1, 10):
                print(mark, 'Please enter a valid move')
                display_board(key)
                continue
            index = key.index(mark)
            key[index] = ' '
            break
        except:
            print('Available keys as follows')
            display_board(key)
            print('Please enter correct number to place your move according to the left moves on grid\t')
    board[mark] = move[turn[i]]


def make_board():
    return ['#'] + [' '] * 9, ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]


def map_player_to_marker(player1, player2):
    return {'Player_1': player1, 'Player_2': player2}, ['Player_1', 'Player_2'], randint(0, 1)


def game():
    player1, player2 = decide_player(None, None)

    board, key = make_board()
    move, turn, turn_index = map_player_to_marker(player1,player2)

    while True:
        play(turn_index, turn, board, key, move)

        game_over, winner = result(board)
        if game_over:
            display_board(board)
            break
        turn_index = (turn_index + 1) % 2

    print('GAME OVER::')
    if winner == 'X' or winner == 'O':
        print(winner, 'is winner')
    else:
        print('Game is', winner)


def replay():
    print('Do you want to replay??\nPress y for YES and any  other key for NO\t')
    response = input()
    return response.lower() == 'y'


def tic_tac_toe():
    game()

    if replay():
        tic_tac_toe()


tic_tac_toe()