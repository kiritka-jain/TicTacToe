from typing import List


def print_grid(grid: List) -> None:
    """
    Prints the grid

    :param grid: Grid to be printed
    :return:  None
    """
    # TODO: beautify print
    for row in grid:
        for column in row:
            print(column, end='')
        print()


grid = [['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']]


def terminate_game(chance: int) -> bool:
    """
    check if game needs to be terminated or not
    :param chance: no. of chances played in the game
    :return: bool
    """
    if chance > 9:
        return True
    return False

chance = 0
while True:
    chance += 1
    # TODO: Check game status
    if terminate_game(chance):
        break
    print_grid(grid)
    print('---------------------------------------------------------')
    if chance % 2 == 0:
        print('Player 2 to play\n')
        i,j = map(int,input().split())
        grid[i-1][j-1] = 'X'
    else:
        print('Player 1 to play\n')
        i,j = map(int,input().split())
        grid[i-1][j-1] = 'O'

