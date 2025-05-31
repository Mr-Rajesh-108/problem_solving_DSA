class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def findMaxFork(root, k):
    result = None
    while root:
        if root.data <= k:
            result = root.data
            root = root.right
        else:
            root = root.left
    return result if result is not None else -1

def build_tree_from_list(s):
    if not s or s[0] == 'N':
        return None
    values = s.strip().split()
    root = Node(int(values[0]))
    queue = [root]
    index = 1

    while queue and index < len(values):
        node = queue.pop(0)

        if index < len(values) and values[index] != 'N':
            node.left = Node(int(values[index]))
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] != 'N':
            node.right = Node(int(values[index]))
            queue.append(node.right)
        index += 1

    return root

def run_example(tree_list, k):
    s = ' '.join(str(x) for x in tree_list)
    root = build_tree_from_list(s)
    return findMaxFork(root, k)


# Example 1
print(run_example([10, 7, 15, 2, 8, 11, 16], 14))  # Output: 11

# Example 2
print(run_example([5, 2, 12, 1, 3, 9, 21, 'N', 'N', 'N', 'N', 'N', 'N', 19, 25], 24))  # Output: 21

# Example 3
print(run_example([5, 2, 12, 1, 3, 9, 21, 'N', 'N', 'N', 'N', 'N', 'N', 19, 25], 4))   # Output: 3

