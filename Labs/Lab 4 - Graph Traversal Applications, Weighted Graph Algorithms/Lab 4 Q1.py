def adjacency_list(graph_str):
    """Returns the adjacency list for a textual graph given."""
    graph_list = graph_str.splitlines()
    graph_info = graph_list[0].split()
    adj_list = [[] for i in range(int(graph_info[1]))]
    
    for i in range(1, len(graph_list)):
        edge = graph_list[i].split()
        first = int(edge[0])
        second = int(edge[1])
        if len(edge) == 3:
            weight = int(edge[2])
        else:
            weight = None
        adj_list[first].append((second, weight))
        if graph_info[0] == 'U':
            adj_list[second].append((first, weight))
    
    return adj_list


def transpose(adj_list):
    """Returns the transpose of an adjacency list."""
    transpose_list = [[] for i in range(len(adj_list))]
    for i, vertex in enumerate(adj_list):
        for edge in vertex:
            transpose_list[edge[0]].append((i, edge[1]))
    return transpose_list


graph_string = """\
D 3
0 1
1 0
0 2
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))
    
graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))
    
    # It should also work undirected graphs.
    # The output will be the same as input.
    
graph_string = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))
    
graph_string = """\
U 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

graph_adj_list = adjacency_list(graph_string)
graph_transposed_adj_list = transpose(graph_adj_list)
for i in range(len(graph_transposed_adj_list)):
    print(i, sorted(graph_transposed_adj_list[i]))