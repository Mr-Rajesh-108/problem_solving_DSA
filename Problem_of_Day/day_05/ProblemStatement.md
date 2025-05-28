# 🟢 Find Rectangle with Corners as 1

**Difficulty**: Medium  
**Accuracy**: 56.75%

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

## ✅ Python Solution

```python
def has_rectangle_with_ones(mat):
    if not mat or not mat[0]:
        return False

    rows = len(mat)
    cols = len(mat[0])
    seen_pairs = set()

    for i in range(rows):
        ones = [j for j in range(cols) if mat[i][j] == 1]

        # Check all pairs of 1s in the current row
        for x in range(len(ones)):
            for y in range(x + 1, len(ones)):
                pair = (ones[x], ones[y])
                if pair in seen_pairs:
                    return True
                seen_pairs.add(pair)

    return False

```

---

## 🧪 Example Usage

```python

mat1 = [
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1]
]
mat2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

print(has_rectangle_with_ones(mat1))  # Output: True
print(has_rectangle_with_ones(mat2))  # Output: False
```

---

## ✅ Output

```
True
False
```
