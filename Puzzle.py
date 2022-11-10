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

    # find shortest path
    steps.sort(key=len)
    steps = steps[0]

    # make tuple route
    route = route_construct(Source, steps)

    # done!
    return route, steps


def _solver(board, source, dest, seen, steps):

    if source == dest:
        return [steps]                                      # we win

    cur_steps = []

    neighbors = _adjacents(board, source)

    for neigh in neighbors:
        if neigh[0] not in seen:
            seen.add(neigh[0])
            temp = _solver(board, neigh[0], dest, seen, steps + neigh[1])
            if temp:
                cur_steps += temp
            seen.discard(neigh[0])
    return cur_steps


def route_construct(source, steps):
    """
    Takes source and steps to ending, returns list of tuples of the path
    :param source: Source node
    :param steps: U/D/L/R movements used to reach destination
    :return: List of tuples of visited nodes in graph.
    """

    # start route, curr location at source
    route = [source]
    cur_x = source[0]
    cur_y = source[1]

    # iterate and append
    for step in steps:
        if step == "R":
            cur_y += 1
        elif step == "L":
            cur_y -= 1
        elif step == "U":
            cur_x -= 1
        elif step == "D":
            cur_x += 1
        route.append((cur_x, cur_y))

    return route


def _adjacents(puzzle, source):
    """
    Calculates adjacent squares, and the direction to get there
    :param puzzle: Pussle array
    :param source: Square to check from
    :return: list of tuples of allowable moves, form [[(x,y), D], [(x1,y1), D]], where D = UDLR movement.
    """
    # Size of given 2d array
    n = len(puzzle)
    m = len(puzzle[0])

    x = source[0]
    y = source[1]

    # result list
    results = []

    # Checking for all the possible adjacent positions; adding to results if they are
    # Appends [(x, y), "DIR"] for each allowable neighbor

    if _is_valid_position(x, y+1, n, m, puzzle):
        results.append([(x, y+1), "R"])
    if _is_valid_position(x+1, y, n, m, puzzle):
        results.append([(x+1, y), "D"])
    if _is_valid_position(x, y-1, n, m, puzzle):
        results.append([(x, y-1), "L"])
    if _is_valid_position(x-1, y, n, m, puzzle):
        results.append([(x-1, y), "U"])

    # done
    return results


def _is_valid_position(x, y, width, height, puzzle):
    """
    Returns 0 or 1 depending on whether the position is allowable.
    :param x: x coord of target
    :param y: y coord of target
    :param width: width of array
    :param height: height of array
    :param puzzle: puzzle array
    :return: 0 if position is invalid, 1 if position is valid
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