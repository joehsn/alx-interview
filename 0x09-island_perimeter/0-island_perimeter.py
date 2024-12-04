#!/usr/bin/python3
""" 0. Island Perimeter module.
"""


def island_perimeter(grid) -> int:
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 0 represents
        water and 1 represents land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Check all four sides
                # Top
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Bottom
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
