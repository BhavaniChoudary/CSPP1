'''
Tic-Tac_Toe
'''
def horizontal_m(grid):
    '''
        Checks if winner is in horizontal row
    '''
    if grid[0][0] == grid[0][1] == grid[0][2]:
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2]:
        return grid[1][0]
    if grid[2][0] == grid[2][1] == grid[2][2]:
        return grid[2][0]

def vertical_m(grid):
    '''
        Checks if winner is in vertical row
    '''
    if grid[0][0] == grid[1][0] == grid[2][0]:
        return grid[0][0]
    if grid[0][1] == grid[1][1] == grid[2][1]:
        return grid[0][1]
    if grid[0][2] == grid[1][2] == grid[2][2]:
        return grid[0][2]

def diagonal_m(grid):
    '''
        Checks if winner is in diagonal row
    '''
    if grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]

def is_valid_grid(grid):
    '''
        Checks if the grid is valid
    '''
    for inputs in grid:
        for j in inputs:
            if j in ('x', 'o', '.'):
                pass
            else:
                return False
    return True

def is_valid_game(grid):
    '''
        Checks if game is valid
    '''
    count_x = 0
    count_o = 0
    count_dot = 0
    for inputs in grid:
        for j in inputs:
            if j == 'x':
                count_x += 1
            elif j == 'o':
                count_o += 1
            elif j == '.':
                count_dot += 1
    if abs(count_x - count_o >= 2):
        return False
    elif abs(count_x - count_o == 0) and count_dot > 0:
        return False


def main():
    '''
        This is main function
    '''

    if valid_grid is True:
        winner = horizontal_m(grid)
    if winner is None:
            winner = vertical_m(grid)
        if winner is None:
        	winner = diagonal_check(grid)
        if winner is None:
            print("draw")
        else:
            print(winner)
    else:
        if not is_valid_grid(grid):
            print("invalid input")
        if  not is_valid_game(grid):
            print("invalid game")
