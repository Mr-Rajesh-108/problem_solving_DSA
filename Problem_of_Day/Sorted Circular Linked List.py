class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_sorted_circular(head, data):
    new_node = Node(data)

    # Case 1: Empty list
    if not head:
        new_node.next = new_node
        return new_node

    current = head
    while True:
        # Normal case: Insert between two nodes
        if current.data <= data <= current.next.data:
            break

        # Wrap-around case: insert before the smallest or after the largest
        if current.data > current.next.data:
            if data >= current.data or data <= current.next.data:
                break

        current = current.next
        # If we have looped through the whole list
        if current == head:
            break

    # Insert new_node between current and current.next
    new_node.next = current.next
    current.next = new_node

    # If the new node should be the new head (i.e., smallest value)
    if data < head.data:
        return new_node
    return head

def print_circular_list(head):
    if not head:
        print("List is empty.")
        return
    result = []
    current = head
    while True:
        result.append(str(current.data))
        current = current.next
        if current == head:
            break
    print(" ".join(result))

# 🔍 Build input list: 48 -> 49 -> 53 -> 54 -> 61 (circular)
values = [48, 49, 53, 54, 61]
nodes = [Node(val) for val in values]
for i in range(len(nodes)):
    nodes[i].next = nodes[(i + 1) % len(nodes)]
head = nodes[0]

print("Original list:")
print_circular_list(head)

# ✅ Insert 11
head = insert_sorted_circular(head, 11)

print("After inserting 11:")
print_circular_list(head)
