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


def bfs_tree(adj_list, start):
    if len(adj_list) == 0:
        return []
    parent_list = [None] * len(adj_list)
    vertices = deque()
    vertices.append(start)
    while len(vertices) != 0:
        current = vertices.pop()
        for edge in adj_list[current]:
            vertex = edge[0]
            if parent_list[vertex] == None and vertex != start:
                parent_list[vertex] = current
                vertices.appendleft(vertex)
    return parent_list


print(bfs_tree([[(0, None)]], 0))


# an undirected graph

adj_list = [
    [(1, None)],
    [(0, None), (2, None)],
    [(1, None)]
]

print(bfs_tree(adj_list, 0))
print(bfs_tree(adj_list, 1))

# a directed graph (note the asymmetrical adjacency list)

adj_list = [
[(1, None)],
[]
]

print(bfs_tree(adj_list, 0))
print(bfs_tree(adj_list, 1))

graph_string = """\
D 2
0 1
"""

print(bfs_tree(adjacency_list(graph_string), 0))

graph_string = """\
D 2
0 1
1 0
"""

print(bfs_tree(adjacency_list(graph_string), 1))

# graph from the textbook example
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

print(bfs_tree(adjacency_list(graph_string), 1))

graph_string = """\
D 2 W
0 1 99
"""

print(bfs_tree(adjacency_list(graph_string), 0))

# an undirected graph

adj_list = [
    [(3, None), (1, None)],
    [(0, None), (2, None)],
    [(3, None), (1, None)],
    [(0, None), (2, None)]
]

for s in range(4):
    print(bfs_tree(adj_list, s))
    
# graph from the textbook example
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

print(bfs_tree(adjacency_list(graph_string), 1))

graph_string = """\
U 4
0 1
1 2
2 3
3 0
"""

print(bfs_tree(adjacency_list(graph_string), 0))