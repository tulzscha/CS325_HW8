# Andrew Bear
# CS325 Homework 8
# Puzzle Traversal Assignment.

import heapq


# DFS

def solve_puzzle(Board, Source, Destination):

    # seen = set of coords
    # steps = string
    seen = set()
    steps = ""

    # call function
    steps = _solver(Board, Source, Destination, seen, steps)

    # if no solutions, return None
    if not steps:
        return None

    steps.sort(key=len)

    return steps


def _solver(board, source, dest, seen, steps):

    if source == dest:
        return [steps]                                      # we win

    cur_steps = []

    neighbors = _adjacents(board, source, seen)

    for neigh in neighbors:
        if neigh[0] not in seen:
            seen.add(neigh[0])
            temp = _solver(board, neigh[0], dest, seen, steps + neigh[1])
            if temp:
                cur_steps += temp
            seen.discard(neigh[0])
    return cur_steps


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
    if puzzle[x][y] == "#": # or (x, y) in seen:
        return 0
    return 1


Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
    ]

print(solve_puzzle(Puzzle, (0,0), (4,4)))

Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
    ]

print(solve_puzzle(Puzzle, (4,0), (4,4)))

Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['#', '-', '#', '#', '-'],
    ['-', '#', '-', '-', '-']
    ]

print(solve_puzzle(Puzzle, (0,2), (2,2)))