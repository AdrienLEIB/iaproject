from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMAN = -1
COMP = +1
board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, -1, 0],
    [0, 0, -1, 0, 0],
    [0, -1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
win_state = []
moves = {
    # 1: [0, 0], 2: [0, 1], 3: [0, 2],
    # 4: [1, 0], 5: [1, 1], 6: [1, 2],
    # 7: [2, 0], 8: [2, 1], 9: [2, 2],
}
grilles = 5

def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

# 0 1 2 3 4
# 0 |x| | | | | -> x
# 1 | |x| | | |
# 2 | | |x| | |
# 3 | | | |x| |
# 4 | | | | | |
#    y


def create_win_state(state):
    """
    """
    global win_state
    for iy in range(len(state)):
        for ix in range(len(state[iy])):
            #print(f'pos {iy} _ {ix}')
            check_all_direction(state, iy, ix)
            print(state[iy][ix])
    print(win_state)


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
        # [state[0][0], state[0][1], state[0][2]], # possibilité de victoire 
        # [state[1][0], state[1][1], state[1][2]],
        # [state[2][0], state[2][1], state[2][2]],
        # [state[0][0], state[1][0], state[2][0]],
        # [state[0][1], state[1][1], state[2][1]],
        # [state[0][2], state[1][2], state[2][2]],
        # [state[0][0], state[1][1], state[2][2]],
        # [state[2][0], state[1][1], state[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False


def check_all_direction(state, posy, posx):
    """
    """
    global win_state
    win_state.append(check_at_the_right(state, posy, posx))

    # print(f'result : {right}')
    # print("initiale left verification ...")
    # left = check_at_the_left(state, posy, posx)
    # win_sate.append(check_at_the_left(state, posy, posx))


    # print(f'result : {left}')
    # print("initiale top verification ...")
    # top = check_at_the_top(state, posy, posx)
    # win_sate.append(check_at_the_top(state, posy, posx))
    # print(f'result : {top}')



    # print("initiale bot verification ...")
    # bot = check_at_the_bot(state, posy, posx)
    # print(f'result : {bot}')
    # win_sate.append(check_at_the_bot(state, posy, posx))

    # print("initiale diago RIGHT TOP verification ...")
    # rt = check_at_the_diagonal_rt(state, posy, posx)
    # print(f'result : {rt}')
    # win_sate.append(check_at_the_diagonal_rt(state, posy, posx))

    # print("initiale diago RIGHT BOT verification ...")
    # rb = check_at_the_diagonal_rb(state, posy, posx)
    # print(f'result : {rb}')
    # win_sate.append(check_at_the_diagonal_rb(state, posy, posx))


    # print("initiale diago left TOP verification ...")
    # lt = check_at_the_diagonal_lt(state, posy, posx)
    # print(f'result : {lt}')
    # win_sate.append(check_at_the_diagonal_lt(state, posy, posx))

    # print("initiale diago left BOT verification ...")
    # lb = check_at_the_diagonal_lb(state, posy, posx)
    # print(f'result : {lb}')
    # win_sate.append(check_at_the_diagonal_lb(state, posy, posx))

    # print("____________________________________________________")

    # if True in win_sate:
    #     return True
    # else:
    #     return False





def gen_possibility_to_win(moves):
    """
    """

    return "t"

def check_at_the_right(state, posy, posx):
    """
    """
    checkR = []
    if posx + 3 < grilles:
        for i in range(4):
            checkR.append(state[posy][posx+i])
        return checkR
    else:
        pass





def check_at_the_left(state, posy, posx):
    """
    """
    value = state[posy][posx]
    checkL = []
    if posx - 3 >= 0:
        i = posx
        while (i >= posx-3):
            checkL.append(state[posy][i])
            i-=1
    else:
        return False

    if [value,value,value, value] == checkL:
        return True
    else:
        return False

def check_at_the_top(state, posy, posx):
    """
    """
    value = state[posy][posx]
    checkT = []
    if posy - 3 >= 0:
        i = posy
        while (i >= posy-3):
            checkT.append(state[i][posx])
            i-=1
    else:
        return False

    if [value,value,value, value] == checkT:
        return True
    else:
        return False


def check_at_the_bot(state, posy, posx):
    """
    """
    value = state[posy][posx]
    checkB = []
    if posy + 3 < grilles:
        for i in range(4):
            checkB.append(state[posy+1][posx])
    else:
        return False

    if [value,value,value, value] == checkB:
        return True
    else:
        return False

def check_at_the_diagonal_rt(state, posy, posx):
    """
    """
    value = state[posy][posx]
    checkRT = []
    if posy - 3 >= 0 and posx + 3 < grilles:
        i = posy
        ix = 0
        while (i >= posy-3):
            checkRT.append(state[i][posx+ix])
            i-=1
            ix+=1
    else:
        return False

    if [value,value,value, value] == checkRT:
        return True
    else:
        return False

def check_at_the_diagonal_rb(state, posy, posx):
    """
    """
    value = state[posy][posx]
    checkRB = []
    if posy + 3 < grilles and posx + 3 < grilles:
        for i in range(4):
            checkRB.append(state[posy+1][posx+1])
    else:
        return False

    if [value,value,value, value] == checkRB:
        return True
    else:
        return False


def check_at_the_diagonal_lb(state, posy, posx):
    """
    """
    value = state[posy][posx]
    checkLB = []

    if posy + 3 < grilles and  posx - 3 >= 0:
        iy = 0
        ix = posx
        while (ix >= posx-3):
            checkLB.append(state[posy+iy][ix])
            iy+=1
            ix-=1
    else:
        return False

    if [value,value,value, value] == checkLB:
        return True
    else:
        return False

def check_at_the_diagonal_lt(state, posy, posx):
    """
    """
    value = state[posy][posx]
    checkLT = []

    if posy - 3 >= 0 and  posx - 3 >= 0:
        iy = posy
        ix = posx
        while (iy >= posy-3):
            checkLT.append(state[iy][ix])
            iy-=1
            ix-=1
    else:
        return False

    if [value,value,value, value] == checkLT:
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
            print(check_all_direction(board, coord[0], coord[1]))
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


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
    grilles = 5# the dimension of grilles


    create_win_state(board)

    # moves = gen_moves(grilles)



    # # Human chooses X or O to play
    # while h_choice != 'O' and h_choice != 'X':
    #     try:
    #         print('')
    #         h_choice = input('Choose X or O\nChosen: ').upper()
    #     except (EOFError, KeyboardInterrupt):
    #         print('Bye')
    #         exit()
    #     except (KeyError, ValueError):
    #         print('Bad choice')

    # # Setting computer's choice
    # if h_choice == 'X':
    #     c_choice = 'O'
    # else:
    #     c_choice = 'X'

    # # Human may starts first
    # clean()
    # while first != 'Y' and first != 'N':
    #     try:
    #         first = input('First to start?[y/n]: ').upper()
    #     except (EOFError, KeyboardInterrupt):
    #         print('Bye')
    #         exit()
    #     except (KeyError, ValueError):
    #         print('Bad choice')



    # human_turn(c_choice, h_choice)
        # ai_turn(c_choice, h_choice)

    # Game over message
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

    # exit()

if __name__ == '__main__':
    main()