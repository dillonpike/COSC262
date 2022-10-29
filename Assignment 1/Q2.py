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


def bubbles(physical_contact_info):
    adj_list = adjacency_list(physical_contact_info)
    state = [False] * len(adj_list)
    components = []
    for i in range(len(adj_list)):
        if state[i] is False:
            parent = dfs_tree(adj_list, i)
            bubble = [i]
            state[i] = True
            for i in range(len(parent)):
                if parent[i] is not None:
                    bubble.append(i)
                    state[i] = True
            components.append(bubble)
    return components
    
    
physical_contact_info = """\
U 2
0 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 2
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 7
1 2
1 5
1 6
2 3
2 5
3 4
4 5
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 0
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

physical_contact_info = """\
U 1
"""

print(sorted(sorted(bubble) for bubble in bubbles(physical_contact_info)))

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

print(sorted(sorted(bubble) for bubble in bubbles(graph_string)))
