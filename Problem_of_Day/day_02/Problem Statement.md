# Pythagorean Triplet

**Difficulty:** Medium  **Average Time:** 20m

---

## Problem Statement

Given an array `arr[]`, return `true` if there is a **triplet (a, b, c)** from the array (where `a`, `b`, and `c` are on different indexes) that satisfies the condition: `a² + b² = c²`

Otherwise, return `false`.

---

## Examples

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
