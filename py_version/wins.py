board = [
    [1, 1, 0, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# check if player wins with it's last move
def wins(state, last_move, player):
    posx = last_move[0] 
    posy = last_move[1] 

    return check_line_and_col(state, posx, posy, player) or check_diago_right(state, posx, posy, player) or check_diago_left(state, posx, posy, player)

# check line and column
def check_line_and_col(state, posx, posy, player):
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

# check diagonal from top right
def check_diago_right(state, posx, posy, player):
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

# check diagonal from top left
def check_diago_left(state, posx, posy, player):
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


def main():
    last_move = [1, 3]
    player = 1


    print(wins(board, last_move, player))



if __name__ == '__main__':
    main()

