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

def next_vertex(in_tree, distance):
    minimum = (float('inf'), None)
    for i in range(len(distance)):
        if distance[i] < minimum[0] and in_tree[i] == False:
            minimum = (distance[i], i)
    return minimum[1]

def dijkstra(adj_list, start):
    n = len(adj_list)
    in_tree = [False] * n
    distance = [float('inf')] * n
    parent = [None] * n
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        if u is None:
            break
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if not in_tree[v] and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return parent, distance
    
    
    
graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""

print(dijkstra(adjacency_list(graph_string), 1))
print(dijkstra(adjacency_list(graph_string), 2))

graph_string = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(dijkstra(adjacency_list(graph_string), 0))
print(dijkstra(adjacency_list(graph_string), 2))