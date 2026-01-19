class Node: # Definition for a binary tree node.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def preorder_traversal(root): # Root, Left, Right
    if root!=None:
        print(root.value, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root): # Left, Root, Right
    if root!=None:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

def postorder_traversal(root): # Left, Right, Root
    if root!=None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=' ')
        
        
# Example usage:
if __name__ == "__main__": 
    
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right=Node(6)

    print("Inorder Traversal:")
    inorder_traversal(root)  # Output: 4 2 5 1 3
    print("\nPreorder Traversal:")
    preorder_traversal(root)  # Output: 1 2 4 5 3
    print("\nPostorder Traversal:")
    postorder_traversal(root)  # Output: 4 5 2 3 1
