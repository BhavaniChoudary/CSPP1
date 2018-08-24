def horizontal_check(grid):
    '''
        Checks if winner is in horizontal row
    '''
    if grid[0][0] == grid[0][1] == grid[0][2]:
        return grid[0][0]
    if grid[1][0] == grid[1][1] == grid[1][2]:
        return grid[1][0]
    if grid[2][0] == grid[2][1] == grid[2][2]:
        return grid[2][0]

def verical_check(grid):
    '''
        Checks if winner is in vertical row
    '''
    if grid[0][0] == grid[1][0] == grid[2][0]:
        return grid[0][0]
    if grid[0][1] == grid[1][1] == grid[2][1]:
        return grid[0][1]
    if grid[0][2] == grid[1][2] == grid[2][2]:
        return grid[0][2]


def main():
    '''
        This is main function
    '''

    if valid_grid is True:
        winner = horizontal_check(grid)
    if winner is None:
            winner = verical_check(grid)
        if winner is None:   
