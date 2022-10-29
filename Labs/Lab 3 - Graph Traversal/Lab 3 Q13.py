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


def dfs_tree(adj_list, start):
    if len(adj_list) == 0:
        return []
    parent_list = [None] * len(adj_list)
    dfs_loop(adj_list, start, start, parent_list)
    return parent_list

    
def dfs_loop(adj_list, start, current, parent_list):
    for edge in adj_list[current]:
        vertex = edge[0]
        if parent_list[vertex] == None and vertex != start:
            parent_list[vertex] = current
            dfs_loop(adj_list, start, vertex, parent_list)


# an undirected graph

adj_list = [
    [(1, None), (2, None)],
    [(0, None), (2, None)],
    [(0, None), (1, None)]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))
print(dfs_tree(adj_list, 2))

# a directed graph (note the asymmetrical adjacency list)

adj_list = [
[(1, None)],
[]
]

print(dfs_tree(adj_list, 0))
print(dfs_tree(adj_list, 1))

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

print(dfs_tree(adjacency_list(graph_string), 1))

gstring = """\
U 4
2 3
2 1
0 3
1 0
"""

print(dfs_tree(adjacency_list(gstring), 0))

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

print(dfs_tree(adjacency_list(graph_string), 1))