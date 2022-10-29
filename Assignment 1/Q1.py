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


def format_sequence(converters_info, source_format, destination_format):
    adj_list = adjacency_list(converters_info)
    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            adj_list[i][j] = (adj_list[i][j][0], 1)
    parent, distance = dijkstra(adj_list, source_format)
    sequence = [destination_format]
    while sequence[-1] != source_format:
        current = parent[sequence[-1]]
        if current == None:
            return 'No solution!'
        sequence.append(current)
    sequence.reverse()
    return sequence
    
    
converters_info_str = """\
D 2
0 1
"""

source_format = 0
destination_format = 1

print(format_sequence(converters_info_str, source_format, destination_format))

converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 1))

converters_info_str = """\
D 2
0 1
"""

print(format_sequence(converters_info_str, 1, 0))

converters_info_str = """\
D 5
1 0
0 2
2 3
1 2
"""

print(format_sequence(converters_info_str, 1, 2))

converters_info_str = """\
D 1
"""

print(format_sequence(converters_info_str, 0, 0))

converters_info_str = """\
D 17
"""

print(format_sequence(converters_info_str, 0, 0))