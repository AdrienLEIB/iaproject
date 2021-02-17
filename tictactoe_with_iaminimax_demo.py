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
    [0,0,0,0,0],
    [0,0,0,0,0]
]

moves = {
    1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3], 5: [0, 4], 
    6: [1, 0], 7: [1, 1], 8: [1, 2], 9: [1, 3], 10: [1, 4]
}

grilles = 0
comboforWin = 0


def genere_params_for_win(grilles):
    if grilles == 3:
        comboforWin = 3
    else:
        comboforWin = 4
    return comboforWin

def check_the_line(state, posx, posy):
    """
    """
    line = []
    if posy + (comboforWin-1) < grilles:
        for i in range(comboforWin):
            line.append(state[posx][posy+i])
        return line

    return


def check_the_column(state, posx, posy):
    """
    """
    column = []
    if posx + (comboforWin-1) < grilles:
        for i in range(comboforWin):
            column.append(state[posx][posy])
            posx+=1
        return column

    return

def check_diago_bottom(state, posx, posy):
    """
    """
    x = posx
    y = posy
    try:
        if comboforWin == 3:
            diagoB =  [state[x][y], state[x+1][y+1], state[x+2][y+2]]
        elif comboforWin == 4:
            diagoB =  [state[x][y], state[x+1][y+1], state[x+2][y+2], state[x+3][y+3]]
        return diagoB
    except:
        pass
    
    return 

def check_diago_top(state, posx, posy):
    """
    """
    x = posx
    y = posy
    
        
    try:
        if x - (comboforWin-1) >= 0 and comboforWin==3:
            diagoT =  [state[x][y], state[x-1][y+1], state[x-2][y+2]]
        elif x - (comboforWin-1) >= 0 and comboforWin==4:
            diagoT =  [state[x][y], state[x-1][y+1], state[x-2][y+2],state[x-3][y+3] ]
        return diagoT
    except:
        pass
    
    return 


def create_win_possibility(state):
    wins_state = []
    for x in range(len(state)):
        for y in range(len(state)):
            line = check_the_line(state, x, y)
            if line:
                wins_state.append(line)
    
            column = check_the_column(state, x, y)
            if column:
                wins_state.append(column)
            diago_bottom = check_diago_bottom(state, x, y)
            if diago_bottom:
                wins_state.append(diago_bottom)
                
            diago_top = check_diago_top(state, x, y)
            if diago_top:
                wins_state.append(diago_top)
    return wins_state

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


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X X X] or [O O O]
    * Three cols    [X X X X X] or [O O O]
    * Two diagonals [X X X X X]
                    [X X X X X] or [O O O]
                    [X X X X X]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    #win_state = create_win_possibility(state)

    win_state = [[ state[0][0] ,  state[0][1] ,  state[0][2] ,  state[0][3] ],
 [ state[0][1] ,  state[0][2] ,  state[0][3] ,  state[0][4] ],
 [ state[1][0] ,  state[1][1] ,  state[1][2] ,  state[1][3] ],
 [ state[1][1] ,  state[1][2] ,  state[1][3] ,  state[1][4] ]]

    if comboforWin == 3 and [player, player, player] in win_state:
        return True
    elif comboforWin == 4 and [player, player, player, player] in win_state:
        return True
    else:
        return False

def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, HUMAN) or wins(state, COMP)


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


def minimax(state, depth, player):
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


    if depth == 0 or game_over(state):
        score = evaluate(state)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player)
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
    if depth == 0 or game_over(board):
        return

    
    print(f'Computer turn [{c_choice}]')

    render(board, c_choice, h_choice)



    if depth == 10:
        x_lenght = []
        y_lenght = []
        for indice in range(grilles):
            x_lenght.append(indice)
            y_lenght.append(indice)
        x = choice(x_lenght)
        y = choice(y_lenght)
    else:
        move = minimax(board, depth, COMP)
        x, y = move[0], move[1]

    set_move(x, y, COMP)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    """
    The Human plays choosing a valid move.
    :param c_choice: computer's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    

    #clean()
    print(f'Human turn [{h_choice}]')
    render(board, c_choice, h_choice)
    movespossible = "Use numpad 1.. 10: "
    while move < 1 or move > 10:
        try:
            move = int(input(movespossible))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN)
            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def gen_moves(grilles):
    pos = 1
    for i in range(grilles):
        for j in range(grilles):
            moves[pos] = [i, j]
            pos += 1
  
    return moves


def main():
    """
    Main function that calls all functions
    """
    #clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first
    global grilles
    global comboforWin

    grilles = 2

    
    comboforWin = genere_params_for_win(grilles)

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
    #clean()
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
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)


    # Game over message
    if wins(board, HUMAN):
        #clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP):
        #clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        #clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()
