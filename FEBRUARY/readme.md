```markdown
# Distinct Occurrences

## Problem Description

Given two strings `s` and `t` of lengths `n` and `m` respectively. Find the count of distinct occurrences of `t` in `s` as a sub-sequence modulo 10^9 + 7.

## Examples

### Example 1:

**Input:**
```

s = "banana"
t = "ban"

```

**Output:**
```

3

```

**Explanation:**
There are 3 sub-sequences: [ban], [ba n], [b an].

### Example 2:

**Input:**
```

s = "geeksforgeeks"
t = "ge"

```

**Output:**
```

6

```

**Explanation:**
There are 6 sub-sequences: [ge], [ge], [g e], [g e] [g e] and [g e].

## Your Task

You don't need to read input or print anything. Your task is to complete the function `subsequenceCount()` which takes two strings as arguments (`s` and `t`) and returns the count of the sub-sequences modulo 10^9 + 7.

## Constraints

- 1 ≤ n, m ≤ 1000

## Expected Complexity

- Expected Time Complexity: O(n * m)
- Expected Auxiliary Space: O(n * m)

---

```
