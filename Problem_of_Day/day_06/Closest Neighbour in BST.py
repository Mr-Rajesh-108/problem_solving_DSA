class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def find_max_leq_k(self, root, k):
        result = None
        while root:
            if root.data <= k:
                result = root.data
                root = root.right
            else:
                root = root.left
        return result

def build_tree_from_list(values):
    if not values or values[0] is None:
        return -1

    root = Node(values[0])
    queue = [root]
    index = 1

    while queue and index < len(values):
        node = queue.pop(0)

        if index < len(values) and values[index] is not None:
            node.left = Node(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = Node(values[index])
            queue.append(node.right)
        index += 1

    return root

# Create solution instance
sol = Solution()

# Example 1
tree1 = build_tree_from_list([10, 7, 15, 2, 8, 11, 16])
print(sol.find_max_leq_k(tree1, 14))  # Output: 11

# Example 2
tree2 = build_tree_from_list([5, 2, 12, 1, 3, 9, 21, None, None, None, None, None, None, 19, 25])
print(sol.find_max_leq_k(tree2, 24))  # Output: 21

# Example 3
print(sol.find_max_leq_k(tree2, 4))   # Output: 3
