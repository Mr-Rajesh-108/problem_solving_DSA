class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
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
        
        while t.next != None:
            t = t.next
        else:
            t.next = temp
            temp.prev = t


    def printLL(self): # Display all elements in the list as a Python list:
        t1= self.head
        while t1.next != None: # Traverse to the last node
            print(t1.data, end=' ')
            t1= t1.next 
        print(t1.data)

    def insertAtbeg(self, value): # Insert a new node with the given value at the beginning of the list:
        temp = Node(value)
        if self.head == None:
            self.head = temp
            return
        else:
            temp.next = self.head  # Link new node to the former head
            self.head.prev = temp
            self.head = temp # Update head to new node


    def insertInMiddle(self, value, x): # Insert a new node with the given value after the first occurrence of x:
        t1 = self.head
        while t1.next != None:
            if t1.data == x:
                break
            else: t1 = t1.next   
        temp = Node(value)
        temp.next = t1.next # Link new node to the next node
        t1.next.prev = temp
        t1.next = temp # Link current node to new node
        temp.prev = t1
        
    def deleteLL(self, value): # Delete the first occurrence of a node with the given value from the list:
        if self.head == None:
            print("List is empty")
            return
        t1 = self.head
        if t1.data == value:  # If the head node is to be deleted
            self.head = t1.next
            self.head.prev = None
            return
        while t1.next != None:
            if t1.data == value:
                t1.prev.next = t1.next  # Bypass the node to delete
                t1.next.prev = t1.prev
                return
            else:
                t1 = t1.next
        if t1.data == value:  # Check if the last node is to be deleted
            t1.prev.next = None
        


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
