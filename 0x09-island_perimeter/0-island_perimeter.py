#!/usr/bin/python3
"""0x09. Island Perimeter"""


def island_perimeter(grid: list[list[int]]) -> int:
    """island_perimeter function"""
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
