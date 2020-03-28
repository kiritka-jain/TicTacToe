from typing import List


def print_grid(grid: List) -> None:
    """
    Prints the grid

    :param grid: Grid to be printed
    :return:  None
    """
    for row in grid:
        for column in row:
            print(column, end='')
        print()


grid = [['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']]
print_grid(grid)
