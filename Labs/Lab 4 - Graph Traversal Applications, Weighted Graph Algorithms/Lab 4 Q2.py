from collections import deque

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


def bfs_loop(adj_list):
    """Performs a bfs on an adj_list and returns the state list."""
    state = ['D'] + ['U' for i in range(len(adj_list)-1)]
    vertices = deque()
    vertices.append(0)
    while len(vertices) != 0:
        current = vertices.pop()
        for edge in adj_list[current]:
            vertex = edge[0]
            if state[vertex] == 'U':
                vertices.appendleft(vertex)
        state[current] = 'P'
    return state
    
    
def is_strongly_connected(adj_list):
    """Returns True if a graph is strongly connected, otherwise False."""
    if len(adj_list[0]) == 0:
        return False
    state = bfs_loop(adj_list)
    for vertex in state:
        if vertex != 'P':
            return False
    transposed = transpose(adj_list)
    state = bfs_loop(transposed)
    for vertex in state:
        if vertex != 'P':
            return False
    return True


graph_string = """\
D 3
0 1
1 0
0 2
"""

print(is_strongly_connected(adjacency_list(graph_string)))

graph_string = """\
D 3
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))

graph_string = """\
D 4
0 1
1 2
2 0
"""

print(is_strongly_connected(adjacency_list(graph_string)))

# Since we are passing an adjacency list to your algorithm,
# it will see an un directed graph as a directed one where each
# undirected edge appears as two directed edges.

graph_string = """\
U 5
2 4
3 1
0 4
2 1
"""

print(is_strongly_connected(adjacency_list(graph_string)))