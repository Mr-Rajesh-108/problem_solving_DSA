class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

    def insert(root, value):  # Insert a new node with the given value into the BST:
        if root == None:
            return Node(value)
        if root.data == value:
            return root  # Duplicate values are not inserted in the BST 

        if root.data > value:
            root.left = Node.insert(root.left, value)
        else:
            root.right = Node.insert(root.right, value)
        return root
    
    def inOrder(root):  # Perform in-order traversal of the BST and print the node values:
        if root != None:
            Node.inOrder(root.left)
            print(root.data, end=' ')
            Node.inOrder(root.right)
            
    def search(root, value):  # Search for a node with the given value in the BST:
        if root == None or root.data == value:
            return root
        if root.data > value:
            return Node.search(root.left, value)
        else:
            return Node.search(root.right, value) 


# Example usage: 
root = Node.insert(None, 20)
root = Node.insert(root, 15)
root = Node.insert(root, 30)
root = Node.insert(root, 40)
root = Node.insert(root, 12)
root = Node.insert(root, 18)
root = Node.insert(root, 25)
root = Node.insert(root, 50)

Node.inOrder(root) # Output: 12 15 18 20 25 30 40 50

element = Node.search(root,18)
print("\nFound:", element.data) if element else print("\nNot Found")
element = Node.search(root,100)
print("\nFound:", element.data) if element else print("\nNot Found")
