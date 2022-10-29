# Do not alter the next two lines
from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

# Rewrite the following function to avoid slicing
def binary_search_tree(nums, start=0, end=-1, is_sorted=False):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums is already sorted.
       Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
    if end == -1:
        end = len(nums) - 1
    if start >= end:
        tree = Node(nums[start], None, None)  # A leaf
    else:
        mid = (end - start + 1) // 2 + start  # Halfway (approx)
        left = binary_search_tree(nums, start, mid-1, True)
        right = binary_search_tree(nums, mid, end, True)
        tree = Node(nums[mid - 1], left, right)
    return tree
    
# Leave the following function unchanged
def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)

nums = [22, 41, 19, 27, 12, 35, 14, 20,  39, 10, 25, 44, 32, 21, 18]
tree = binary_search_tree(nums)
print_tree(tree)

nums = [228]
tree = binary_search_tree(nums)
print_tree(tree)

nums = [228, 227, 3]
tree = binary_search_tree(nums)
print_tree(tree)