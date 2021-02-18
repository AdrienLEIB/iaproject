board = [
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]


# check if player wins
def wins(state, player):
    grid_length = len(state)
    mid_pos_x, mid_pos_y = int(grid_length / 2), int(grid_length / 2)
    for i in range(grid_length - 1):
        if check_line(state, i, mid_pos_y, player) or check_diago_left(state, i, mid_pos_y, player) or check_diago_right(state, i, mid_pos_y, player) or check_column(state, mid_pos_x, i, player):
                return True
    
    return False


# check line 
def check_line(state, posx, posy, player):
    for i in range(len(state) - 3):
        line = [state[posx][i], state[posx][i+1], state[posx][i+2], state[posx][i+3]]
        if [player, player, player, player] == line:
            return True
    
    return False

# check column
def check_column(state, posx, posy, player):
    for i in range(len(state) - 3):
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


""" def main():
    player = 1
    print(wins(board, player))



if __name__ == '__main__':
    main()
 """
