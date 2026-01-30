class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item): # Add an item to the front of the deque
        self.items.append(item)

    def add_rear(self, item): # Add an item to the back of the deque
        self.items.insert(0, item)

    def remove_front(self): # Remove and return the item from the front of the deque
        if not self.is_empty():
            return self.items.pop() 
        raise IndexError("remove_front from empty deque")

    def remove_rear(self): # Remove and return the item from the back of the deque
        if not self.is_empty():
            return self.items.pop(0) 
        raise IndexError("remove_rear from empty deque")

    def size(self): # Return the number of items in the deque
        return len(self.items)
    
    def print_deque(self):
        print(self.items)

deque = Deque()
deque.add_rear(10)
deque.add_rear(20)
deque.add_front(30)
deque.add_front(40)
deque.print_deque()
print(deque.remove_front())
print(deque.remove_rear())
print(deque.remove_front())
deque.print_deque()
