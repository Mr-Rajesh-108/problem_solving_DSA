class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
    
class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):  # Append a new node with the given value to the end of the list:
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        t = self.head
        
        while t.right != None:
            t = t.right
        else:
            t.right = temp
            temp.left = t


    def printLL(self): # Display all elements in the list as a Python list:
        t1= self.head
        while t1.right != None: # Traverse to the last node
            print(t1.data, end=' ')
            t1= t1.right 
        print(t1.data)

    def insertAtbeg(self, value): # Insert a new node with the given value at the beginning of the list:
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        else:
            temp.right = self.head  # Link new node to the former head
            self.head.left = temp
            self.head = temp # Update head to new node


    def insertInMiddle(self, value, x): # Insert a new node with the given value after the first occurrence of x:
        t1 = self.head
        while t1.right != None:
            if t1.data == x:
                break
            else: t1 = t1.right   
        temp = Node(value)
        temp.right = t1.right # Link new node to the next node
        t1.right.left = temp
        t1.right = temp # Link current node to new node
        temp.left = t1
        
    def deleteLL(self, value): # Delete the first occurrence of a node with the given value from the list:
        if self.head == None:
            print("List is empty")
            return
        t1 = self.head
        if t1.data == value:  # If the head node is to be deleted
            self.head = t1.right
            self.head.left = None
            return
        while t1.right != None:
            if t1.data == value:
                t1.left.right = t1.right  # Bypass the node to delete
                t1.right.left = t1.left
                return
            else:
                t1 = t1.right
        if t1.data == value:  # Check if the last node is to be deleted
            t1.left.right = None
        


# Example usage:
dll = DoublyLinkedList()

dll.insertAtEnd(10)
dll.insertAtEnd(20)
dll.insertAtEnd(30)
dll.insertAtEnd(40)

dll.printLL()  # Output: 10 20 30 40
dll.insertAtbeg(5)
dll.printLL()  # Output: 5 10 20 30 40

dll.insertInMiddle(25,20)
dll.printLL()  # Output: 5 10 20 25 30 40
dll.deleteLL(25)
dll.printLL()  # Output: 5 10 20 30 40  
