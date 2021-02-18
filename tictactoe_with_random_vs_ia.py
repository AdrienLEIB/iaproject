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

IA = -1
RANDOM = +1

chars = {
    -1: 'X',
    +1: 'O',
    0: ' '
}

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluate(state):
    """
    Function to heuristic evaluation of state.
    :param state: the state of the current board
    :return: +1 if the computer wins; -1 if the human wins; 0 draw
    """
    if wins(state, IA):
        score = +1
    elif wins(state, RANDOM):
        score = -1
    else:
        score = 0

    return score


def wins(state, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param state: the state of the current board
    :param player: a human or a computer
    :return: True if the player wins
    """
    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def game_over(state):
    """
    This function test if the human or computer wins
    :param state: the state of the current board
    :return: True if the human or computer wins
    """
    return wins(state, RANDOM) or wins(state, IA)


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
    if player == IA:
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

        if player == IA:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best



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

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, IA)
        x, y = move[0], move[1]

    set_move(x, y, IA)


def random_turn():
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return
    
    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = choice(empty_cells(board))
        x, y = move[0], move[1]
    
    set_move(x, y, RANDOM)



def game(first):
    # Main loop of this game
    global board

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    if first != 'X' and first != 'O':
        print('bad choice X/O')
        exit()
    
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first.upper() == 'X':
            ai_turn()
            first = ''

        random_turn()
        ai_turn()

    # Game over message
    if wins(board, RANDOM):
        return 1
    elif wins(board, IA):
        return -1
    else:
        return 0


def main():
    ia_wins = 0
    random_wins = 0
    draw = 0

    # lancer 1000 parties
    for i in range(500):
        ia_start = game('X')
        random_start = game('O')

        if ia_start == 1:
            random_wins += 1
        elif ia_start == -1:
            ia_wins += 1
        else:
            draw += 1

        if random_start == 1:
            random_wins += 1
        elif random_start == -1:
            ia_wins += 1
        else:
            draw += 1

    print('IA wins: ', ia_wins)
    print('Random wins: ', random_wins)
    print('Draw: ', draw)



if __name__ == '__main__':
    main()

