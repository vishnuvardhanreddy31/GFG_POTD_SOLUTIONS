# N-th Character After Iterations

## 09-03-2024

## Problem Statement

Given a binary string `s`, perform `r` iterations on string `s`, where in each iteration 0 becomes 01 and 1 becomes 10. Find the nth character (considering 0-based indexing) of the string after performing these `r` iterations.

### Example

#### Input:

```python
s = "1100"
r = 2
n = 3
```

#### Output:

```python
1
```

**Explanation:**

After the 1st iteration, `s` becomes "10100101".
After the 2nd iteration, `s` becomes "1001100101100110".
Now, we can clearly see that the character at the 3rd index is 1, and so the output.

#### Input:

```python
s = "1010"
r = 1
n = 2
```

#### Output:

```python
0
```

**Explanation:**

After the 1st iteration, `s` becomes "10011001".
Now, we can clearly see that the character at the 2nd index is 0, and so the output.

### Constraints

- 1 ≤ |s| ≤ 103
- 1 ≤ r ≤ 20

## Task

Your task is to complete the function `nthCharacter()` which takes the string `s` and integers `r` and `n` as input parameters and returns the n-th character of the string after performing `r` operations on `s`.

### Expected Time Complexity

O(r\*|s|)

### Expected Auxiliary Space

O(|s|)

## Python Solution

```python
class Solution:
    def nthCharacter(self, s, r, n):
        while r > 0:
            m = ""
            for i in range(min(len(s), n+1)):
                if s[i] == '1':
                    m += "10"
                else:
                    m += "01"

            s = m
            r -= 1

        return s[n]
```
