# Andrew Bear
# CS325 Homework 8
# Puzzle Traversal Assignment.

import heapq

# DFS

def solve_puzzle(Board, Source, Destination, seen = None, directions = None):
    """

    :param Board:
    :param Source:
    :param Destination:
    :return:
    """


    #_puzzle(Board, Source, Destination, )

    pass

#
# traversal - recursive(G, s):
# mark s as visited
# for all neighbours w of s in Graph G:
#   if w is not visited:
#     traversal - recursive(G, w)


def _adjacents(puzzle, x, y, seen):

    # Size of given 2d array
    n = len(puzzle)
    m = len(puzzle[0])

    # result list
    results = []

    # Checking for all the possible adjacent positions; adding to results if they are
    # Appends [(x, y), effort] for each allowable neighbor
    if _is_valid_position(x - 1, y, n, m):
        results.append([(x - 1, y), abs(puzzle[x][y] - puzzle[x - 1][y])])
    if _is_valid_position(x + 1, y, n, m):
        results.append([(x + 1, y), abs(puzzle[x][y] - puzzle[x + 1][y])])
    if _is_valid_position(x, y - 1, n, m):
        results.append([(x, y - 1), abs(puzzle[x][y] - puzzle[x][y - 1])])
    if _is_valid_position(x, y + 1, n, m):
        results.append([(x, y + 1), abs(puzzle[x][y] - puzzle[x][y + 1])])

    # done
    return results

def _is_valid_position(x, y, puzzle, seen ):
    """

    :param x:
    :param y:
    :param puzzle:
    :param seen:
    :return:
    """
    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return 0
    return 1

Puzzle = [
 ['-', '-', '-', '-', '-'],
 ['-', '-', '#', '-', '-'],
 ['-', '-', '-', '-', '-'],
 ['#', '-', '#', '#', '-'],
 ['-', '#', '-', '-', '-']
]