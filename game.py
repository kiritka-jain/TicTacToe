from typing import List, Tuple


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


def terminate_game(chance: int) -> bool:
    """
    check if game needs to be terminated or not
    :param chance: no. of chances played in the game
    :return: bool
    """
    if chance > 9:
        return True
    return False


def valid_input(i: int, j: int, grid: List) -> bool:
    """
    check if the input is valid
    :param i: row index
    :param j: column index
    :param grid: grid
    :return: bool
    """
    if not (0 < i and i < 4 and 0 < j and j < 4):
        print('You should enter valid coordinates')
        return False
    if grid[i-1][j-1] != '.':
        print('the cell is already occupied')
        return False
    return True


def get_input(grid:List)-> Tuple:
    """
    gets input from user until it's valid
    :param grid: grid
    :return: cell coordinates
    """
    while True:
        i, j = map(int, input().split())
        if valid_input(i, j, grid):
            return i,j


if __name__ == '__main__':

    grid = [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]

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
            i, j = get_input(grid)
            grid[i - 1][j - 1] = 'X'
        else:
            print('Player 1 to play\n')
            i, j = get_input(grid)
            grid[i - 1][j - 1] = 'O'
