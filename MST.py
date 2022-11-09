# Andrew Bear
# CS325 Homework 8
# Minimum Spanning Tree

import heapq




def Prims(G):
    """

    :param G:
    :return:
    """
    # num vertexes
    num_v = len(G)

    # Create lists
    dist = [float("infinity") for _ in G]
    prev = [None for _ in G]
    visited = []
    MST = []


    # initialize start
    dist[0] = 0
    prev[0] = 0


    # create heap
    pq = []

    # initialize heap with starting values
    for n in range(1, num_v):
        if G[0][n] > 0:
            heapq.heappush(pq, (G[0][n], n, 0))


    print(dist)
    print(prev)


    while len(visited) < num_v:
        current_node = heapq.heappop(pq)
        MST.append((current_node[2], current_node[1], current_node[0]))


        neighbors = []
        for n in range(num_v):
            if G[current_node[1]][n] > 0:
                if n not in visited:
                    neighbors.append(n)
                    heapq.heappush(pq, (G[current_node[1]][n], n, current_node[1]))

       # for node in neighbors:

        visited.append(current_node[1])


        print(MST)
        print(neighbors)
        print(pq)

     #   break
    #     CurrentNode = unvisited vertex v with smallest dist[v]
    #     MST.add((prevNode, CurrentNode))
    #     for node in CurrentNode.neighbours:
    #         dist[node] = min(w(CurrentNode, node), dist[node])
    #         if dist[node] updated: prev[node] = CurrentNode
    #     visited.add(CurrentNode)
    # return MST

    pass
    

"""
    s <- pick a source vertex from V

    for v in V: #v: current vertex; V: all the vertices in G
        dist[v] = infinity
        prev[v] = Empty

    #initalize source
    dist[v] = 0
    prev[v] = s

    #update neighbouring nodes of s
    for node in s.neighbours
        dist[v] = weight of (s,node)
        prev[v] = s

    while(len(visited)<len(V)):
        CurrentNode = unvisited vertex v with smallest dist[v]
        MST.add((prevNode, CurrentNode))
        for node in CurrentNode.neighbours:
            dist[node] = min(w(CurrentNode, node), dist[node])
            if dist[node] updated: prev[node] = CurrentNode
        visited.add(CurrentNode)
    return MST



"""

G = [
 [0, 8, 5, 0, 0, 0, 0],
 [8, 0, 10, 2, 18, 0, 0],
 [5, 10, 0, 3, 0, 16, 0],
 [0, 2, 3, 0, 12, 30, 14],
 [0, 18, 0, 12, 0, 0, 4],
 [0, 0, 16, 30, 0, 0, 26],
 [0, 0, 0, 14, 4, 26, 0]
]


Prims(G)