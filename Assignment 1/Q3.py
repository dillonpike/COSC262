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


def dfs_loop(adj_list, start, state, stack):
    for edge in adj_list[start]:
        vertex = edge[0]
        if state[vertex] == 'U':
            state[vertex] = 'D'
            dfs_loop(adj_list, vertex, state, stack)
    state[start] = 'P'
    stack.append(start)


def build_order(dependencies):
    adj_list = adjacency_list(dependencies)
    state = ['U' for i in range(len(adj_list))]
    stack = []
    for i in range(len(adj_list)):
        if state[i] == 'U':
            dfs_loop(adj_list, i, state, stack)
    stack.reverse()
    return stack
    
    
dependencies = """\
D 2
0 1
"""

print(build_order(dependencies))

dependencies = """\
D 3
1 2
0 2
"""

print(build_order(dependencies) in [[0, 1, 2], [1, 0, 2]])

dependencies = """\
D 3
"""
# any permutation of 0, 1, 2 is valid in this case.
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))

graph_string = """\
D 17
1 2
1 15
1 6
12 13
2 15
13 4
4 5
"""

print(build_order(graph_string))