class Node:
    def __init__(self, data, next=None ):
        self.data = data
        self.next = next
        
class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtEnd(self, value):  # Append a new node with the given value to the end of the list:
        temp = Node(value)
        if self.head != None:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp


    def printLL(self): # Display all elements in the list as a Python list:
        t1= self.head
        while t1.next != None: # Traverse to the last node
            print(t1.data)
            t1= t1.next 
        print(t1.data)
        
    def insertAtbeg(self, value): # Insert a new node with the given value at the beginning of the list:
        temp = Node(value)
        if self.head != None:
            temp.next = self.head  # Link new node to the former head
            self.head = temp # Update head to new node
        else:
            self.head = temp    
            

    def insertInMiddle(self, value, x): # Insert a new node with the given value after the first occurrence of x:
        temp = Node(value)
        t1 = self.head
        while t1.next != None:
            if t1.data == x:
                temp.next = t1.next # Link new node to the next node
                t1.next = temp # Link current node to new node
                return
            t1 = t1.next

    def deleteLL(self, value): # Delete the first occurrence of a node with the given value from the list:
        t1 = self.head
        prev = t1
        if t1.data == value:  # If the head node is to be deleted
            self.head = t1.next
            return
        while t1.next != None:
            if t1.data == value:
                prev.next = t1.next  # Bypass the node to delete
                return
            prev = t1
            t1 = t1.next
        if t1.data == value:  # Check if the last node is to be deleted
            prev.next = None   

sll= SinglyLinkedList()
sll.insertAtEnd(10)
sll.insertAtEnd(20)
sll.insertAtEnd(30)
sll.insertAtEnd(40)
sll.insertAtbeg(15)
sll.insertAtbeg(5)
sll.insertInMiddle(25,20)
sll.printLL()

sll.deleteLL(25)
print("After deletion:")
sll.printLL()