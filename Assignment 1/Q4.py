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


def prim(adj_list, start):
    num = len(adj_list)
    in_tree = [False] * num
    distance = [float('inf') for i in range(num)]
    parent = [None] * num
    distance[start] = 0
    while not all(in_tree):
        current = next_vertex(in_tree, distance)
        in_tree[current] = True
        for vertex, weight in adj_list[current]:
            if not in_tree[vertex] and weight < distance[vertex]:
                distance[vertex] = weight
                parent[vertex] = current
    return parent, distance    

def which_segments(city_map):
    adj_list = adjacency_list(city_map)
    parent, distance = prim(adj_list, 0)
    segments = []
    for i in range(1, len(parent)):
        if i < parent[i]:
            segments.append((i, parent[i]))
        else:
            segments.append((parent[i], i))
    return segments


city_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_segments(city_map)))

city_map = """\
U 1 W
"""

print(sorted(which_segments(city_map)))
