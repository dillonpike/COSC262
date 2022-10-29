from pprint import pprint

def adjacency_matrix(graph_str):
    """Returns the adjacency matrix for a textual graph given."""
    graph_list = graph_str.splitlines()
    graph_info = graph_list[0].split()
    
    if len(graph_info) == 3:
        weight = None
    else:
        weight = 0
        
    vertices = int(graph_info[1])
    adj_matrix = [[weight for i in range(vertices)] for i in range(vertices)]
    
    if len(graph_info[1].split()) != 3:
        weight = 1
    
    for i in range(1, len(graph_list)):
        edge = graph_list[i].split()
        first = int(edge[0])
        second = int(edge[1])
        if len(edge) == 3:
            weight = int(edge[2])
        adj_matrix[first][second] = weight
        if graph_info[0] == 'U':
            adj_matrix[second][first] = weight
        
    return adj_matrix
    
graph_string = """\
D 0
"""
print(adjacency_matrix(graph_string))
    
graph_string = """\
D 3
0 1
1 0
0 2
"""

print(adjacency_matrix(graph_string))

graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
print(adjacency_matrix(graph_string))

graph_string = """\
U 7
1 2
1 5
1 6
3 4
0 4
4 5
"""

pprint(adjacency_matrix(graph_string))

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

pprint(adjacency_matrix(graph_string))