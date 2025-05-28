
# 🟢 Find Rectangle with Corners as 1

**Difficulty**: Medium  
**Accuracy**: 56.75%  
**Submissions**: 19K+  
**Points**: 4

---

## 🧠 Problem Statement

Given an `n x m` binary matrix `mat[][]` containing only `0`s and `1`s, determine if there exists a **rectangle** within the matrix such that **all four corners** of the rectangle are `1`.  
If such a rectangle exists, return `true`; otherwise, return `false`.

---

## 🔍 Test Cases

### ✅ Example 1

**Input:**
```python
mat = [
  [1, 0, 0, 1, 0],
  [0, 0, 1, 0, 1],
  [0, 0, 0, 1, 0], 
  [1, 0, 1, 0, 1]
]
```

**Output:**
```
true
```

**Explanation:**  
Valid corners are at indices (1,2), (1,4), (3,2), (3,4).

---

### ✅ Example 2

**Input:**
```python
mat = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
```

**Output:**
```
false
```

**Explanation:**  
There are no valid corners with all 1s.

---

## 📌 Constraints

- `1 ≤ n, m ≤ 200`  
- `0 ≤ mat[i][j] ≤ 1`

---
