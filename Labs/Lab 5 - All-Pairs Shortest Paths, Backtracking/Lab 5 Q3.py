from graphs import adjacency_list
import copy

def distance_matrix(adj_list):
    matrix = [[float('inf') for i in range(len(adj_list))] for i in range(len(adj_list))]
    for i, vertex in enumerate(adj_list):
        matrix[i][i] = 0
        for edge in vertex:
            matrix[i][edge[0]] = edge[1]
    return matrix

def floyd(distance):
    dist = []
    for row in distance:
        dist.append(row[:])
    length = len(dist)
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
    
    
graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

adj_list = adjacency_list(graph_str)
dist_matrix = distance_matrix(adj_list)
dist = floyd(dist_matrix)
print("Initial distance matrix:", dist_matrix)
print("Shortest path distances:", dist)

import pprint

graph_str = """\
U 7 W
0 1 5
0 2 7
0 3 12
1 2 9
2 3 4
1 4 7
2 4 4
2 5 3
3 5 7
4 5 2
4 6 5
5 6 2
"""

pprint.pprint(floyd(distance_matrix(adjacency_list(graph_str))))