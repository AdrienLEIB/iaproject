from math import inf as infinity
from random import choice
import platform
import time
from os import system
from wins import wins


PL = -1 # O 
IA = +1 # X

chars = {
    -1: 'O',
    +1: 'X',
    0: ' '
}

board = [
    [+1, +1, +0, +0, +0],
    [-0, -1, +0, +1, +1],
    [+0, +0, +1, +0, +0],
    [+1, -1, +0, -1, +1],
    [+0, +1, -1, +0, +0],
]

# board = []

grid_len = 0

def empty_cells(state):
    """
    Each empty cell will be added into cells' list
    :param state: the state of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells



def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, IA):
        score = +1
    elif wins(state, PL):
        score = -1
    else:
        score = 0
    return score



def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

# init the board 
def init_borad(grid_length):
    global board
    board = [[0] * grid_length for i in range(grid_length)]
    global grid_len
    grid_len = grid_length



def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def render(state):
    """
    Print the board on console
    :param state: current state of the board
    """
    str_line = ''
    cols = '    '
    for i in range(len(state)):
        cols += str(i) + '    '
        str_line += '-----'
    print('\n'+ cols)
    print('  ' + str_line)
    i = 0
    for row in state:
        j = True
        for cell in row:
            symbol = chars[cell]
            if j :
                print(f'{i} | {symbol} |', end='')
                j = False
            else:
                print(f'| {symbol} |', end='')
        i += 1
        print('\n' + '  ' + str_line)
    

def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, PL) or wins(state, IA) 


###############################################################################################
########################################### ALPHA_BETA ########################################
###############################################################################################

def alpha_beta(state, depth, alpha, beta, player):
    row = -1
    col = -1
    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]


    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = alpha_beta(state, depth - 1, alpha, beta, -player)

        if player == IA:
            if score[2] > alpha:
                alpha = score[2]
                row = cell[0]
                col = cell[1]
        else:
            if score[2] < beta:
                beta = score[2]
                row = cell[0]
                col = cell[1]

        state[x][y] = 0

        if alpha >= beta:
            break
    
    if player == IA:
        return [row, col, alpha]
    else:
        return [row, col, beta]


###############################################################################################
########################################### IA TURN ###########################################
###############################################################################################

def ai_turn():
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Computer turn [{chars[IA]}]')
    render(board)
    if depth == grid_len * grid_len:
        x = choice(range(grid_len))
        y = choice(range(grid_len))
    else:
        move = alpha_beta(board, depth, -infinity, infinity, IA)
        x, y = move[0], move[1]

    set_move(x, y, IA)
    time.sleep(1)


###############################################################################################
########################################### HUMAN TURN ########################################
###############################################################################################

def human_turn():
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'Human turn [{chars[PL]}]')
    render(board)

    x = -1
    y = -1
    while x < 0 or x > grid_len - 1 or y < 0 or y > grid_len - 1:
        try:
            x = int(input('Use numpad x: '))
            y = int(input('Use numpad y: '))
            can_move = set_move(x, y, PL)
            if not can_move:
                print('Bad move')
                x = -1
                y = -1
            else:
                return
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

###############################################################################################
########################################### MAIN ##############################################
###############################################################################################


def main():
    """ clean()
    grid_length = int(input('Choose your grid length (5X5), (7X7)...  :  '))
    while grid_length % 2 == 0:
        grid_length = int(input('Choose your grid length (5X5), (7X7)... (odd number)  :  '))

    print('initializing the board...\n')
    init_borad(grid_length) """

    # Human may starts first
    first = ''
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn()
            first = ''

        human_turn()
        ai_turn()

    # Game over message
    if wins(board, PL):
        clean()
        print(f'Human turn [{chars[PL]} ]')
        render(board)
        print('YOU WIN!')
    elif wins(board, IA):
        clean()
        print(f'Computer turn [{chars[IA]}]')
        render(board)
        print('YOU LOSE!')
    else:
        clean()
        render(board)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()