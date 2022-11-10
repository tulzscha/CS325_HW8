# Andrew Bear
# CS325 Homework 7
# Minimum Effort Puzzle

import heapq


def solve_puzzle(Board, Source, Destination):

    effort_dic = calculate_effort(Board, Source, Destination)

    if not effort_dic:
        return None

    path = create_trace(effort_dic, Source, Destination)

    return path

def calculate_effort(Board, Source, Destination):
    """
    Returns minimum effort necessary to solve the 3d puzzle contained within "puzzle"
    :param puzzle: puzzle to be solved
    :return: int, minimum effort necessary to solve puzzle
    """
    # length and height
    length = len(Board)
    height = len(Board[0])

    # populate effort dictionary with infinitys
    efforts = dict()
    for i in range(length):
        for j in range(height):
            efforts[(i, j)] = float("infinity")

    efforts[Source[0], Source[1]] = 0                               # overwrite starting effort

    # start priority queue, with effort and coords of top-left
    path = ""

    pq = [(0, (Source[0], Source[1]))]


    # here be a standard-ish Djikstra loop, with a few caveats
    while len(pq) > 0:
        current_effort, current_vertex = heapq.heappop(pq)

        # skip this, because it's a bad path
        if current_effort > efforts[current_vertex]:
            continue

        # return if we reach "lower-right" node
        if current_vertex == (Destination[0], Destination[1]):
            return efforts

        # generate list of adjacent neighbors, and effort values (aka the edges)
        neighbors = _adjacent_elements(Board, current_vertex[0], current_vertex[1])

        # step through the neighbors of the current location
        for neighbor, effort in neighbors:
            # min effort is the max of current, and the effort necessary to reach the neighbor
            min_eff = current_effort + 1

            # test, update, push neighbor
            if min_eff < efforts[neighbor]:
                efforts[neighbor] = min_eff
                heapq.heappush(pq, (min_eff, neighbor))


def create_trace(effort, source, dest):

    moves = []
    visited = []

    cur_node = dest
    cur_eff = effort[dest]

    while cur_eff > 0:
        visited.append(cur_node)

        cur_eff -= 1

        if (cur_node[0] - 1, cur_node[1]) in effort and effort[(cur_node[0] - 1, cur_node[1])] == cur_eff:
            moves.append("D")
            cur_node = (cur_node[0] - 1, cur_node[1])
        elif (cur_node[0] + 1, cur_node[1]) in effort and effort[(cur_node[0] + 1, cur_node[1])] == cur_eff:
            moves.append("U")
            cur_node = (cur_node[0] + 1, cur_node[1])
        elif (cur_node[0], cur_node[1] - 1) in effort and effort[(cur_node[0], cur_node[1] - 1)] == cur_eff:
            moves.append("R")
            cur_node = (cur_node[0], cur_node[1] - 1)
        elif (cur_node[0], cur_node[1] + 1) in effort and effort[(cur_node[0], cur_node[1] + 1)] == cur_eff:
            moves.append("L")
            cur_node = (cur_node[0], cur_node[1] + 1)

    movstring = ""
    for i in range(len(moves)-1, -1, -1):
        movstring += moves[i]

    visited.append(source)
    visited.reverse()

    return visited, movstring


def _is_valid_position(x, y, width, height, puzzle):
    """
    Checks if element x, y is valid position in the 2d array
    :param x: desired x
    :param y: desired y
    :param width: width of array
    :param height: height of array
    :return: 0 if invalid location, 1 if valid location in array
    """
    if x < 0 or y < 0 or x > width - 1 or y > height - 1 or puzzle[x][y] == "#":
        return 0
    return 1


def _adjacent_elements(puzzle, x, y):
    """
    Returns a list of the adjacent elements to a given x, y, in the puzzle, along with the effort required to reach
    each neighbor
    :param puzzle: puzzle array
    :param x: x coordinate
    :param y: y coordinate
    :return: list of neighbors, each in the form [(x,y), effort]
    """
    # Size of given 2d array
    n = len(puzzle)
    m = len(puzzle[0])

    # result list
    results = []

    # Checking for all the possible adjacent positions; adding to results if they are
    # Appends [(x, y), effort] for each allowable neighbor
    if _is_valid_position(x - 1, y, n, m, puzzle):
        results.append([(x-1, y), 1])
    if _is_valid_position(x + 1, y, n, m, puzzle):
        results.append([(x+1, y), 1])
    if _is_valid_position(x, y - 1, n, m, puzzle):
        results.append([(x, y-1), 1])
    if _is_valid_position(x, y + 1, n, m, puzzle):
        results.append([(x, y+1), 1])

    # done
    return results


# Testing section
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

Puzzle = [
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-']
    ]

print(solve_puzzle(Puzzle, (0,0), (4,4)))