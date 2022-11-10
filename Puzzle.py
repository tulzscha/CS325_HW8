# Andrew Bear
# CS325 Homework 8
# Puzzle Traversal Assignment.

import heapq


# DFS

def solve_puzzle(Board, Source, Destination, directions=None, steps=None, seen=None):


    if directions is None:
        directions = []
    if steps is None:
        steps = ""
    if seen is None:
        seen = []


    if Source == Destination:
        return directions, steps                   # we win

    neighbors = _adjacents(Board, Source, seen)

    if not neighbors:                       # no neighbors
        return                              # will this finish out deadending?

    seen.append(Source)
    print(seen)

    pass


#
# traversal - recursive(G, s):
# mark s as visited
# for all neighbours w of s in Graph G:
#   if w is not visited:
#     traversal - recursive(G, w)


def _adjacents(puzzle, source, seen):
    # Size of given 2d array
    n = len(puzzle)
    m = len(puzzle[0])

    x = source[0]
    y = source[1]

    # result list
    results = []

    # Checking for all the possible adjacent positions; adding to results if they are
    # Appends [(x, y), effort] for each allowable neighbor
    if _is_valid_position(x-1, y, n, m, puzzle, seen):
        results.append([(x-1, y), "U"])
    if _is_valid_position(x+1, y, n, m, puzzle, seen):
        results.append([(x+1, y), "D"])
    if _is_valid_position(x, y-1, n, m, puzzle, seen):
        results.append([(x, y-1), "L"])
    if _is_valid_position(x, y+1, n, m, puzzle, seen):
        results.append([(x, y+1), "R"])

    # done
    return results


def _is_valid_position(x, y, width, height, puzzle, seen):
    """

    :param x:
    :param y:
    :param puzzle:
    :param seen:
    :return:
    """

    if x < 0 or y < 0 or x > width - 1 or y > height - 1:
        return 0
    if (x, y) in seen or puzzle[x][y] == "#":
        return 0
    return 1


Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
]

solve_puzzle(Puzzle, (0,0), (4,4) )