# 🟢 Print Leaf Nodes from Preorder Traversal of BST

**Difficulty**: Medium  
**Accuracy**: 47.26%  
---

## 🧠 Problem Statement

Given a preorder traversal of a Binary Search Tree (BST), find the **leaf nodes** of the tree **without building the tree**.

---

## 🔍 Test Cases

### ✅ Example 1

**Input:**
preorder[] = [5, 2, 10]

**Output:** [2, 10]

**Explaination:**

![exp1_img](https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895564/Web/Other/blobid0_1747480179.jpg)

2 and 10 are the leaf nodes as shown in the figure.

---
### ✅ Example 2
**Input:** 
preorder[] = [4, 2, 1, 3, 6, 5]

**Output:** [1, 3, 5]

**Explaination:**

![exp2_img](https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895564/Web/Other/blobid1_1747480193.jpg)

1, 3 and 5 are the leaf nodes as shown in the figure.

---
### ✅ Example 3

**Input:** 
preorder[] = [8, 2, 5, 10, 12]

**Output:** [5, 12]

**Explaination:** 

![exp3_img](https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/895564/Web/Other/blobid2_1747480202.jpg)

5 and 12 are the leaf nodes as shown in the figure.

---
## 🔒 Constraints
- 1 ≤ preorder.size() ≤ 103
- 1 ≤ preorder[i] ≤ 103

---
## ✅ Python Solution
```python
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
```
---
## 🧪 Example Usage
```python
print(find_leaf_nodes([5, 2, 10]))         # Output: [2, 10]
print(find_leaf_nodes([4, 2, 1, 3, 6, 5])) # Output: [1, 3, 5]
print(find_leaf_nodes([8, 2, 5, 10, 12]))  # Output: [5, 12]
```
---
## ✅ Output
```
[2, 10]
[1, 3, 5]
[5, 12]
```
