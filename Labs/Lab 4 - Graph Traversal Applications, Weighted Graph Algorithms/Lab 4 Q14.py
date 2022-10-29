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


def next_vertex(in_tree, distance):
    minimum = (float('inf'), 0)
    for i in range(len(distance)):
        if distance[i] <= minimum[0] and in_tree[i] == False:
            minimum = (distance[i], i)
    return minimum[1]


def dijkstra(adj_list, start):
    num = len(adj_list)
    in_tree = [False] * num
    distance = [float('inf') for i in range(num)]
    parent = [None] * num
    distance[start] = 0
    while not all(in_tree):
        current = next_vertex(in_tree, distance)
        in_tree[current] = True
        for vertex, weight in adj_list[current]:
            if not in_tree[vertex] and distance[current] + weight < distance[vertex]:
                distance[vertex] = distance[current] + weight
                parent[vertex] = current
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