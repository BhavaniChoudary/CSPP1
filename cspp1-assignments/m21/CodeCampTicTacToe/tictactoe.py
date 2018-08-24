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
