from graphs import adjacency_list

def all_paths(adj_list, source, destination):
    solutions = []
    dfs_backtrack((source,), adj_list, destination, solutions)
    return solutions    
    
    
def dfs_backtrack(candidate_path, adj_list, destination, output_data):
    if should_prune(candidate_path):
        return
    if is_solution(candidate_path, destination):
        add_to_output(candidate_path, output_data)
    else:
        for child_candidate_path in children(candidate_path, adj_list):
            dfs_backtrack(child_candidate_path, adj_list, destination, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

def is_solution(candidate_path, destination):
    """Returns True if the candidate is complete solution"""
    return candidate_path[-1] == destination


def children(candidate_path, adj_list):
    """Returns a collestion of candidates that are the children of the given
    candidate."""
    candidates = []
    for edge in adj_list[candidate_path[-1]]:
        if edge[0] not in candidate_path:
            candidates.append(candidate_path + (edge[0],))
    return candidates
    
    
triangle_graph_str = """\
U 3
0 1
1 2
2 0
"""

adj_list = adjacency_list(triangle_graph_str)
print(sorted(all_paths(adj_list, 0, 2)))
print(all_paths(adj_list, 1, 1))

graph_str = """\
U 5
0 2
1 2
3 2
4 2
1 4
"""

adj_list = adjacency_list(graph_str)
print(sorted(all_paths(adj_list, 0, 1)))

from pprint import pprint

# graph used in tracing bfs and dfs
graph_str = """\
D 7
6 0
6 5
0 1
0 2
1 2
1 3
2 4
2 5
4 3
5 4
"""

adj_list = adjacency_list(graph_str)
pprint(sorted(all_paths(adj_list, 6, 3)))    