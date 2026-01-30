class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1
        
    def enqueue(self, value ):  # Add an item to the back of the circular queue
        if (self.rear + 1) % self.size == self.front:
            raise IndexError("enqueue to full circular queue")
        
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = value
            
    def dequeue(self):  # Remove and return the item from the front of the circular queue
        if self.front == -1:
            raise IndexError("dequeue from empty circular queue")
        
        elif self.front == self.rear: 
            print(self.items[self.front])
            self.front = self.rear == -1
        else:
            print(self.items[self.front])
            self.front = ( self.front + 1 ) % self.size
            
    def print_queue(self):
        if self.front == -1:
            print("[]")
            return
        
        index = self.front
        elements = []
        while True:
            elements.append(self.items[index])
            if index == self.rear:
                break
            index = (index + 1) % self.size
        print(elements)
        
    
cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
# cq.enqueue(60) # This should raise an error

cq.print_queue()

cq.dequeue()
cq.dequeue()
cq.enqueue(60)
cq.print_queue()
cq.dequeue()
