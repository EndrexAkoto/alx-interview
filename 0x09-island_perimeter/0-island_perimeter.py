#!/usr/bin/python3
"""
this file define the function island_perimeter
"""


def adjacent_squares(grid, i, j):
    """this function calculates the number of adjacents
    sgaures"""
    count = 0
    row_num = len(grid)
    col_num = len(grid[0])
    if (i > 0 and grid[i-1][j] == 1):
        count += 1
    if (j > 0 and grid[i][j-1] == 1):
        count += 1
    if (i < row_num-1 and grid[i+1][j] == 1):
        count += 1
    if (j < col_num-1 and grid[i][j+1] == 1):
        count += 1
    return count


def island_perimeter(grid):
    """this function returns the perimeter of an island
    described with grid"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                perimeter += 4 - adjacent_squares(grid, i, j)
    return perimeter