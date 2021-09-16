def display_game(game_list):
    # Displaying the TicTacToe Board to players

    print(game_list[0] + ' |' + game_list[1] + ' |' + game_list[2])
    print('--|--|--')
    print(game_list[3] + ' |' + game_list[4] + ' |' + game_list[5])
    print('--|--|--')
    print(game_list[6] + ' |' + game_list[7] + ' |' + game_list[8])

def player_turn():
    # Assigning either X or O to player 1

    play_1 = ''
    while play_1 not in ['X', 'O']:
        play_1 = input('Player 1 "X or O"? \n')
    return play_1

def player_2(player_1):
    # Assiginig the opposite from player one

    if player_1 == 'X':
        play_2 = '0'
    else:
        play_2 = 'X'
    return play_2

def index_pick_player_one():

    # Getting the index from the player 1 to put either 'X' or 'O' on the board
    idx = ''
    while idx not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        idx = input('Player 1 Enter an Index for board(0 to 8):\n')
        if idx in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            idx_a = int(idx)
        else:
            continue
        return idx_a


def index_pick_player_two():
    # Getting the index from the player 2 to put either 'X' or 'O' on the board

    idx2 = ''
    while idx2 not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        idx2 = input('Player 2 Enter an Index for board(0 to 8):\n')
        if idx2 in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            idx2_a = int(idx2)
        else:
            continue
        return idx2_a

def dup_avoid_p1(game_list,idx_a):

    # avoids a new input changing an index if X or O is in it

    if game_list[idx_a] == ' ':
        game_list[idx_a] = p_1
    else:
        while (game_list[idx_a] == ' ') is False:
            idx_a = input('There is a Value in the index you selected... Choose Another Index: \n')
        game_list[idx_a] = p_1

def dup_avoid_p2(game_list,idx2_a):

    # avoids a new input changing an index if X or O is in it

    if game_list[idx2_a] == ' ':
        game_list[idx2_a] = p_2
    else:
        while (game_list[idx2_a] == ' ') is False:
            idx2_a = int(input('There is a Value in the index you selected... Choose Another Index: \n'))
        game_list[idx2_a] = p_2


def check_win(game_list,mark):

    # checks if a player has won

    return ((game_list[0] == game_list[1] == game_list[2] == mark) or
            (game_list[3] == game_list[4] == game_list[5] == mark) or
            (game_list[6] == game_list[7] == game_list[8] == mark) or
            (game_list[0] == game_list[3] == game_list[6] == mark) or
            (game_list[1] == game_list[4] == game_list[7] == mark) or
            (game_list[2] == game_list[5] == game_list[8] == mark) or
            (game_list[0] == game_list[4] == game_list[8] == mark) or
            (game_list[2] == game_list[4] == game_list[6] == mark))

def full_board(game_list):

    # Checks if the board is full

    for i in range(0,9):
        if game_list[i] == ' ':
            return False

    return True

def new_game():

    # To play a new game

    question = ''
    while question not in ['Y','N']:
        question = input('Do You Want To Play Again..? Enter "Y" OR "N"')
    if question == 'Y':
        pass
    else:
        print('Game end')

def random_play():
    from random import randint
    if randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

print('Welcome To TicTacToe')
turn = random_play()
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_game(board)
p_1 = player_turn()
p_2 = player_2(p_1)
game_on = True

while game_on:
    if turn == 'Player 1':
        a = index_pick_player_one()
        dup_avoid_p1(board,a)
        display_game(board)
        if check_win(board,p_1):
            print(f'{p_1} won!!')
            game_on = False
        else:
            full_board(board)
    else:
        b = index_pick_player_two()
        dup_avoid_p2(board,b)
        display_game(board)
        if check_win(board,p_2):
            print(f'{p_2} won!!')
            game_on = False
        else:
            full_board(board)
