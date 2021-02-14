#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

"""
An implementation of Minimax AI Algorithm in Tic Tac Toe,
using Python.
This software is available under GPL license.
Author: Clederson Cruz
Year: 2017
License: GNU GENERAL PUBLIC LICENSE (GPL)
"""

HUMAN = -1
COMP = +1
board = [
    # [0, 0, 0],
    # [0, 0, 0],
    # [0, 0, 0],
]

moves = {
    # 1: [0, 0], 2: [0, 1], 3: [0, 2],
    # 4: [1, 0], 5: [1, 1], 6: [1, 2],
    # 7: [2, 0], 8: [2, 1], 9: [2, 2],
}
grilles = 0

def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, COMP):
        score = +1
    elif wins(state, HUMAN):
        score = -1
    else:
        score = 0

    return score


def wins(state, last_move, player):
    """
    check if player wins with it's last move
    :param state: the state of the current board
    :return: True if the player wins
    """
    posx = last_move[0] 
    posy = last_move[1] 

    return check_line_and_col(state, posx, posy, player) or check_diago_right(state, posx, posy, player) or check_diago_left(state, posx, posy, player)


def check_line_and_col(state, posx, posy, player):
    """
    Check the line and column 
    :param state: the state of the current board
    :param posx: the line indices
    :param posy: the colum indices
    :param player: computer or human
    :return: True if the player have four a suite of 4 pionts
    """

    for i in range(len(state) - 3):
        # check the line
        line = [state[posx][i], state[posx][i+1], state[posx][i+2], state[posx][i+3]]
        if [player, player, player, player] == line:
            return True

        # check the column
        column = [state[i][posy], state[i+1][posy], state[i+2][posy], state[i+3][posy]]
        if [player, player, player, player] == column:
            return True
    
    return False

def check_diago_right(state, posx, posy, player):
    """
    Check the diagonal right going to top
    :param state: the state of the current board
    :param posx: the line indices
    :param posy: the colum indices
    :param player: computer or human
    :return: True if the player have four a suite of 4 pionts
    """
    x = posx
    y = posy
    
    while(x > 0 and y < (len(state)-1)):
        x -= 1
        y += 1
    
    while((y -3) > 0 and (x + 3) <= (len(state)-1)):
        line = [state[x][y], state[x+1][y-1], state[x+2][y-2], state[x+3][y-3]]
        if [player, player, player, player] == line:
            return True
        x += 1
        y -= 1
        
    return False


def check_diago_left(state, posx, posy, player):
    """
    Check the diagonal left going to bot
    :param state: the state of the current board
    :param posx: the line indices
    :param posy: the colum indices
    :param player: computer or human
    :return: True if the player have four a suite of 4 pionts
    """

    x = posx
    y = posy
    
    while(x > 0 and y > 0):
        x -= 1
        y -= 1

    while( (y + 3) <= (len(state)-1) and (x + 3) <= (len(state)-1)):
        line = [state[x][y], state[x+1][y+1], state[x+2][y+2], state[x+3][y+3]]
        if [player, player, player, player] == line:
            return True
        y += 1
        x += 1

    return False

# def game_over(state):
#     """
#     This function test if the human or computer wins
#     :param state: the state of the current board
#     :return: True if the human or computer wins
#     """
#     return wins(state, HUMAN) or wins(state, COMP)


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


def minimax(state, depth, move, player):
    """
    AI function that choice the best move
    :param state: current state of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a computer
    :return: a list with [the best row, best col, best score]
    """
    if player == COMP:
       
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0:
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, move,-player)
        state[x][y] = 0
        score[0], score[1] = x, y

        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(state, c_choice, h_choice):
    """
    Print the board on console
    :param state: current state of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0:
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, COMP)
        
        x, y = move[0], move[1]


    set_move(x, y, COMP)
    if wins(board, move, COMP ):
        return True
    return False
    # time.sleep(1)
    


def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0:
        return

    # Dictionary of valid moves
    move = -1
    

    clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)
    movespossible = "Use numpad 1.." + str(grilles*grilles) + ": "
    while move < 1 or move > (grilles*grilles):
        try:
            move = int(input(movespossible))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)

            if not can_move:
                print('Bad move')
                move = -1
            if wins(board, coord, HUMAN):
                return True
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    return False


def gen_moves(lenght):
    pos = 1
    for i in range(lenght):
        for j in range(lenght):
            moves[pos] = [i, j]
            pos += 1
  
    return moves

def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first
    human_bool = False
    ai_bool = False
    global grilles# the dimension of grilles

    # Human cooses the dimension of board
    while grilles % 2 == 0:
        try:
            print('')
            grilles = int(input("Entrez un nombre impair afin de définir la taille de votre grille: "))
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    for L in range(grilles):
        largeur = []
        for l in range(grilles):
            largeur.append(0)
        board.append(largeur)

    moves = gen_moves(grilles)



    # Human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting computer's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # Human may starts first
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
    while len(empty_cells(board)) > 0 and human_bool != True and ai_bool != True:
        if first == 'N':
            ai_bool = ai_turn(c_choice, h_choice)
            first = ''

        human_bool = human_turn(c_choice, h_choice)
        print(human_bool)
        ai_bool = ai_turn(c_choice, h_choice)


    print("tototo")
    # # Game over message
    # if wins(board, HUMAN):
    #     clean()
    #     print(f'Human turn [{h_choice}]')
    #     render(board, c_choice, h_choice)
    #     print('YOU WIN!')
    # elif wins(board, COMP):
    #     clean()
    #     print(f'Computer turn [{c_choice}]')
    #     render(board, c_choice, h_choice)
    #     print('YOU LOSE!')
    # else:
    #     clean()
    #     render(board, c_choice, h_choice)
    #     print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
