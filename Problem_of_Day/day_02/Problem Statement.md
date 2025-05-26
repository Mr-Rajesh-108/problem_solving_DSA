# Pythagorean Triplet

**Difficulty:** Medium  
**Accuracy:** 24.77%  
**Average Time:** 20m

---

## Problem Statement

Given an array `arr[]`, return `true` if there is a **triplet (a, b, c)** from the array (where `a`, `b`, and `c` are on different indexes) that satisfies the condition: `a² + b² = c²`

Otherwise, return `false`.

---

## Test Cases

### Example 1:

**Input:**  
`arr[] = [3, 2, 4, 6, 5]`  
**Output:**  
`true`  
**Explanation:**  
`a = 3`, `b = 4`, and `c = 5` forms a Pythagorean triplet.

---

### Example 2:

**Input:**  
`arr[] = [3, 8, 5]`  
**Output:**  
`false`  
**Explanation:**  
No such triplet possible.

---

### Example 3:

**Input:**  
`arr[] = [1, 1, 1]`  
**Output:**  
`false`

---

## Constraints

- `1 <= arr.size() <= 10⁵`
- `1 <= arr[i] <= 10³`
---
## ✅ Python Solution
```python
def pythagoreanTriplet(arr):
        squares = set(x * x for x in arr)
        n = len(arr)

        # Try all pairs (a, b) and check if a^2 + b^2 exists in the set
        for i in range(n):
            for j in range(i + 1, n):
                a2_b2 = arr[i]**2 + arr[j]**2
                if a2_b2 in squares:
                    return True
        return False

```
---
## 🧪 Example Usage
```python
arr=[14, 17, 4, 4, 1, 9, 25, 12, 4, 9, 18, 15, 12, 2, 3, 13, 16, 17, 15, 6, 5, 20, 14, 8]
arr1=[3, 2, 4, 6, 5]
arr2=[3,8,5]
arr3=[1,1,1]
print(pythagoreanTriplet(arr))
print(pythagoreanTriplet(arr1))
print(pythagoreanTriplet(arr2))
print(pythagoreanTriplet(arr3))
```
---
## ✅ Output
```
True
True
False
False
```