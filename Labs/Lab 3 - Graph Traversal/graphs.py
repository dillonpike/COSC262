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