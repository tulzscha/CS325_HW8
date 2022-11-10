# Andrew Bear
# CS325 Homework 8
# Minimum Spanning Tree


def Prims(G):
    """
    Returns the Minimum Spanning Tree of graph G.
    :param G: Graph to traverse, in adjacency matrix form.
    :return: List of tuples, where each tuple represents an edge of the MST: (node1, node2, weight).
    """
    # num of vertexes
    num_v = len(G)

    # init the tracking lists and other lists
    dist = [float("infinity")] * num_v
    prev = [None] * num_v
    visited = [False] * num_v                         # convert to booleans for better efficiency
    MST = []

    # seed starting node
    dist[0] = 0
    prev[0] = 0

    # populate neighbors in dist and prev
    for n in range(1, num_v):
        if G[0][n] > 0:
            dist[n] = G[0][n]
            prev[n] = 0

    # Here's the Prim loop -- run n times due to the way 'visited' is built
    for n in range(num_v):

        # here we extract the index of the minimum distance
        minimum = float("infinity")
        for v in range(num_v):                                      # O(n)
            if dist[v] < minimum and not visited[v]:              # constant time
                minimum = dist[v]
                min_index = v

        # add to visited
        visited[min_index] = True

        # add to the MST
        MST.append((prev[min_index], min_index, minimum))

        for v in range(num_v):              # checking all the neighbors (by way of checking all the choices...)
            # If value is present, and less than the current recorded value (and not visited)...
            if 0 < G[min_index][v] < dist[v] and not visited[v]:
                dist[v] = G[min_index][v]       # update the distance to that vertex
                prev[v] = min_index             # update the prev of that vertex to the current index

    MST.remove((0, 0, 0))           # IDK how to NOT add this, so I'll remove it instead.
    return MST

# Test case
# G = [
#  [0, 8, 5, 0, 0, 0, 0],
#  [8, 0, 10, 2, 18, 0, 0],
#  [5, 10, 0, 3, 0, 16, 0],
#  [0, 2, 3, 0, 12, 30, 14],
#  [0, 18, 0, 12, 0, 0, 4],
#  [0, 0, 16, 30, 0, 0, 26],
#  [0, 0, 0, 14, 4, 26, 0]
# ]
# print(Prims(G))
