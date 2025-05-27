# Insert in Sorted Circular Linked List

**Difficulty:** Medium  
**Accuracy:** 25.56%  
**Average Time:** 20 minutes

---

## 🧾 Problem Statement

Given a **sorted circular linked list**, the task is to **insert** a new node into this circular linked list such that it remains **sorted**.

---

## 💡 Test Cases

### Example 1:
**Input:**  
head = 1 → 2 → 4 (circular), data = 2

**Output:**  
1 → 2 → 2 → 4

**Explanation:**  
We can add 2 after the second node.

---

### Example 2:
**Input:**  
head = 1 → 4 → 7 → 9 (circular), data = 5

**Output:**  
1 → 4 → 5 → 7 → 9

**Explanation:**  
We can add 5 after the second node.

---

## 🔒 Constraints

- 2 ≤ number of nodes ≤ 10⁶  
- 0 ≤ node->data ≤ 10⁶  
- 0 ≤ data ≤ 10⁶

---

## ✅ Python Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)

        # Case 1: Empty list
        if not head:
            new_node.next = new_node
            return new_node

        current = head

        while True:
            # Case 2: Insert between two sorted nodes
            if current.data <= data <= current.next.data:
                break

            # Case 3: Insert at the rotation point (max -> min)
            if current.data > current.next.data:
                if data >= current.data or data <= current.next.data:
                    break

            current = current.next

            # Case 4: Came full circle without finding a spot
            if current == head:
                break

        # Insert new node
        new_node.next = current.next
        current.next = new_node

        # Case 5: New node becomes new head (smallest)
        if data < head.data:
            return new_node
        return head
```
---

## 🧪 Example Usage
``` python
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


```
---
## ✅ Output
```
Original list:
48 49 53 54 61
After inserting 11:
11 48 49 53 54 61
```