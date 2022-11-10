# Andrew Bear
# CS325 Homework 8
# Minimum Spanning Tree


def Prims(G):
    """
    Returns the Minimum Spanning Tree of graph G.
    :param G: Graph to traverse, in adjacency matrix form
    :return: List of tuples, where each tuple is represents two nodes and the value of the connecting edge.
    """
    # num of vertexes
    num_v = len(G)

    # init the tracking lists
    dist = [float("infinity")] * num_v
    prev = [None] * num_v

    dist[0] = 0
    prev[0] = 0

    visited = []
    MST = []

    # populate neighbors in dist and prev
    for n in range(1, num_v):
        if G[0][n] > 0:
            dist[n] = G[0][n]
            prev[n] = 0

    # print(dist)
    # print(prev)

    while len(visited) < num_v:

        # here we extract the index of the minimum distance
        minimum = float("infinity")
        for v in range(num_v):
            if dist[v] < minimum and v not in visited:
                minimum = dist[v]
                min_index = v

        # add to visited
        visited.append(min_index)

        # print(visited)
        MST.append((prev[min_index], min_index, minimum))

        for v in range(num_v):

            if G[min_index][v] > 0 and v not in visited and dist[v] > G[min_index][v]:
                dist[v] = G[min_index][v]
                prev[v] = min_index
    #
    # print(dist)
    # print(prev)
    MST.remove((0, 0, 0))
    return MST

G = [
 [0, 8, 5, 0, 0, 0, 0],
 [8, 0, 10, 2, 18, 0, 0],
 [5, 10, 0, 3, 0, 16, 0],
 [0, 2, 3, 0, 12, 30, 14],
 [0, 18, 0, 12, 0, 0, 4],
 [0, 0, 16, 30, 0, 0, 26],
 [0, 0, 0, 14, 4, 26, 0]
]


print(Prims(G))