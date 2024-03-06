#!/usr/bin/python3
"""Defines island perimeter finding function."""


def island_perimeter(grid):
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if j > 0 and grid[i][j - 1] == 1:
                    edges += 1
                if i > 0 and grid[i - 1][j] == 1:
                    edges += 1
    return size * 4 - edges * 2


#!/usr/bin/python3
"""0x09. Island Perimeter"""


def island_perimeter(grid: list[list[int]]) -> int:
    """Return the perimiter of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid."""
    count = 0
    for index, cell in enumerate(grid):
        for ind, sq in enumerate(cell):
            if sq == 1:
                if cell[ind - 1] == 0:
                    if not ind - 1 < 0:
                        count += 1
                if cell[ind + 1] == 0:
                    if not len(cell) - 1 < ind + 1:
                        count += 1
                if grid[index - 1][ind] == 0:
                    if not index - 1 < 0:
                        count += 1
                if grid[index + 1][ind] == 0:
                    if not len(grid) - 1 < index + 1:
                        count += 1

    return count
