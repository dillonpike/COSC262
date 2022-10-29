from math import inf

def next_vertex(in_tree, distance):
    minimum = (float('inf'), 0)
    for i in range(len(distance)):
        if distance[i] <= minimum[0] and in_tree[i] == False:
            minimum = (distance[i], i)
    return minimum[1]
    

in_tree = [False, True, True, False, False]
distance = [float('inf'), 0, 3, 12, 5]
print(next_vertex(in_tree, distance))

in_tree = [False, False, False]
distance = [float('inf'), 0, float('inf')]
print(next_vertex(in_tree, distance))

in_tree = [True, True, True, False, True]
distance = [inf, 0, inf, inf, inf]
print(next_vertex(in_tree, distance))

in_tree = [True, True, True, False, True]
distance = [0, 0, 0, 0, 0]
print(next_vertex(in_tree, distance))