def show_board(board):

    # Displaying of the board

    print(board[1] + '|' + board[2] + '|' + board[3],         '\t1' + '|' + '2' + '|' + '3')
    print(board[4] + '|' + board[5] + '|' + board[6],         '\t4' + '|' + '5' + '|' + '6')
    print(board[7] + '|' + board[8] + '|' + board[9],         '\t7' + '|' + '8' + '|' + '9')

def marker():

    # Assigining of X and O to both players

    mark1 = ''
    while mark1 not in ['X', 'O']:
        mark1 = input('Enter X or O: ')
    if mark1 == 'X':
        return ('X','O')
    else:
        return ('O','X')

def placer(mark):

    # Selection of an Index Between 1 and 9

    while True:
        try:
            pl = int(input(f'Enter a number within 1 and 9 for {mark}: '))
        except:
            print('Not a number Within 1 and 9')
        else:
            if pl not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                continue
            else:
                break
    return pl

def check_space(pl):

    # Checks if the selected index is occupied

    return board[pl] == ' '

def assign(board,pl,mark):

    # Fixing of X or O on the board

    if check_space(pl):
        board[pl] = mark
    else:
        while not check_space(pl):
            print('There is a Value in The Chosen Index')
            pl = placer(mark)
        board[pl] = mark

def full_board():

    # Checks if the board is full

    for i in range(1,10):
        if board[i] == ' ':
            return False
    return True

def check_win(board,mark):

    # Checks for a winner

    return ((board[1]==board[2]==board[3]==mark) or
            (board[4]==board[5]==board[6]==mark) or
            (board[7]==board[8]==board[9]==mark) or
            (board[1]==board[4]==board[7]==mark) or
            (board[2]==board[5]==board[8]==mark) or
            (board[3]==board[6]==board[9]==mark) or
            (board[1]==board[5]==board[9]==mark) or
            (board[3]==board[5]==board[7]==mark))

def random_play():

    # Selects a random starter

    import random
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'

def new_game():

    # To start A new game

    question = ''
    while question not in ['Y','N']:
        question = input('Do You Want To Play Again..? Enter "Y" OR "N":  ').upper()
    return question



print('Welcome To TicTacToe')
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
show_board(board)
p1,p2=marker()
turn = random_play()
game_on = True

while game_on:
    if turn == 'Player 1':
        pl = placer(p1)
        check_space(pl)
        assign(board,pl,p1)
        show_board(board)
        if check_win(board,p1) is True:
            print(f'Congratulations {p1} you won!!')
            if new_game() == 'Y':
                board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
            else:
                game_on = False
        else:
            if full_board() is True:
                print('The game is a draw')
                if new_game() == 'Y':
                    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                    continue
                else:
                    game_on = False
            else:
                turn = 'Player 2'
    else:
        p = placer(p2)
        check_space(p)
        assign(board, p, p2)
        show_board(board)
        if check_win(board, p2) is True:
            print(f'Congratulations {p2} you won!!')
            if new_game() == 'Y':
                board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
                continue
            else:
                game_on = False
        else:
            if full_board() is True:
                print('The game is a draw')
                if new_game() == 'Y':
                    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                    continue
                else:
                    game_on = False
            else:
                turn = 'Player 1'