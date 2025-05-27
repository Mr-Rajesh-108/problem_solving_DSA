def find_leaf_nodes(preorder):
    def helper(start, end):
        if start > end:
            return []

        root = preorder[start]
        split_index = start + 1

        # Find the first node greater than root (right subtree starts here)
        while split_index <= end and preorder[split_index] < root:
            split_index += 1

        # Recursively find leaves in left and right subtree
        left_leaves = helper(start + 1, split_index - 1)
        right_leaves = helper(split_index, end)

        # If both left and right subtrees are empty, this is a leaf
        if not left_leaves and not right_leaves:
            return [root]

        return left_leaves + right_leaves

    return helper(0, len(preorder) - 1)

print(find_leaf_nodes([5, 2, 10]))         # Output: [2, 10]
print(find_leaf_nodes([4, 2, 1, 3, 6, 5])) # Output: [1, 3, 5]
print(find_leaf_nodes([8, 2, 5, 10, 12]))  # Output: [5, 12]
