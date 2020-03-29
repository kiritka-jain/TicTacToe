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


def winning_cond(i: int, j: int, grid: List, symbol: str) -> bool:
    """
    check if winning conditions are met or not
    :param i: row index
    :param j: column index
    :param grid: grid
    :param symbol: either 'X' or 'O'
    :return: bool
    """


    for i in range(3):
        count_row = 0
        count_column = 0
        for j in range(3):
            if grid[j][i] == symbol:
                count_column += 1
            if grid[i][j] == symbol:
                count_row += 1
        if count_column == 3 or count_row == 3:
            return True

    count_diagonal = 0
    count_rev_diagonal = 0

    for i in range(3):
        if grid[i][i] == symbol:
            count_diagonal += 1
        if grid[i][2 - i] == symbol:
            count_rev_diagonal += 1
    if count_diagonal == 3 or count_rev_diagonal == 3:
        return True
    return False


def terminate_game(chance: int) -> bool:
    """
    check if game needs to be terminated or not
    :param chance: no. of chances played in the game
    :return: bool
    """
    if chance > 9:
        print('Its a Draw')
        return True
    # Todo: add winning conditions
    if chance > 4:
        symbol = 'O' if chance % 2 == 1 else 'X'
        result = winning_cond(i, j, grid,symbol)
        if result:
            message = 'Player 1 is winner' if chance % 2 == 1 else 'Player 2 is winner'
            print(message)
        return result
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
    if grid[i - 1][j - 1] != '.':
        print('the cell is already occupied')
        return False
    return True


def get_input(grid: List) -> Tuple:
    """
    gets input from user until it's valid
    :param grid: grid
    :return: cell coordinates
    """
    while True:
        i, j = map(int, input().split())
        if valid_input(i, j, grid):
            return i, j


if __name__ == '__main__':

    grid = [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]

    chance = 0
    while True:
        chance += 1
        # TODO: Check game status
        if terminate_game(chance-1):
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
