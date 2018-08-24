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


def main():
    '''
        This is main function
    '''
    winner = None
    grid = []
    for _ in range(0, 3, 1):
        values = input().split(' ')
        temp = []
        for j in values:
            temp.append(j)
        grid.append(temp)
    valid_grid = is_valid_grid(grid) and is_valid_game(grid)
    if valid_grid is True:
        winner = horizontal_check(grid)
        if winner is None:
            winner = verical_check(grid)
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
