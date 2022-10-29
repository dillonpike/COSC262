def adjacency_list(graph_string):
    header, *edges = [s.split() for s in graph_string.splitlines()]
    directed = header[0] == 'D'
    weighted = len(header) == 3 and header[2] == 'W'
    num_vertices = int(header[1])
    adj_list = [[] for _ in range(num_vertices)]
    for edge in edges:
        edge_data = map(int, edge)
        if weighted:
            source, target, weight = edge_data
        else:
            source, target = edge_data
            weight = None
        adj_list[source].append((target, weight))
        if not directed:
            adj_list[target].append((source, weight))
    return adj_list

def reaching_vertices(adj_list, target):
    vertices = set()
    for j in range(len(adj_list)):
        for i, vertex in enumerate(adj_list):
            if i == target:
                vertices |= {i}
                continue
            for edge in vertex:
                if target == edge[0] or edge[0] in vertices:
                    vertices |= {i}
                    break
    return vertices

graph_string = """\
D 3
0 1
1 0
0 2
"""

adj_list = adjacency_list(graph_string)
print(sorted(reaching_vertices(adj_list, 0)))
print(sorted(reaching_vertices(adj_list, 1)))
print(sorted(reaching_vertices(adj_list, 2)))

graph_string = """\
U 6
0 1
0 2
5 3
"""

adj_list = adjacency_list(graph_string)
for target in range(len(adj_list)):
    print(sorted(reaching_vertices(adj_list, target)))