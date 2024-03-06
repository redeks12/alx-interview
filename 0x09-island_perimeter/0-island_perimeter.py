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
