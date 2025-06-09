def isDeadEnd(root):
    def check(node, min_val, max_val):
        if node is None:
            return False

        # Dead end condition
        if min_val == max_val:
            return True

        # Check left and right subtree
        return (check(node.left, min_val, node.data - 1) or
                check(node.right, node.data + 1, max_val))

    return check(root, 1, float('inf'))

# nodes = ['8', '5', '9', '2', '7', 'N', 'N', '1']
# root = buildTree(nodes)
# print(isDeadEnd(root))  # Output: True
