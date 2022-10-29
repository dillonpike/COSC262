from graphs import adjacency_list

def distance_matrix(adj_list):
    matrix = [[float('inf') for i in range(len(adj_list))] for i in range(len(adj_list))]
    for i, vertex in enumerate(adj_list):
        matrix[i][i] = 0
        for edge in vertex:
            matrix[i][edge[0]] = edge[1]
    return matrix
    
    
graph_str = """\
U 3 W
0 1 5
2 1 7
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))

# more readable output (less readable code):
print("\nEach row on a new line:")
print("\n".join(str(lst) for lst in distance_matrix(adj_list)))

graph_str = """\
D 2 W
0 1 4
"""

adj_list = adjacency_list(graph_str)
print(distance_matrix(adj_list))