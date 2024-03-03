# Largest Number formed from an Array

## 03-03-2024

## Problem Statement:

Given an array of strings `arr[]` of length n representing non-negative integers, arrange them in a manner, such that, after concatenating them in order, it results in the largest possible number. Since the result may be very large, return it as a string.

### Input:

- `n` (1 <= n <= 10^5): Size of the array.
- `arr[]`: An array of strings where each element (1 <= len(arr[i]) <= 18) represents a non-negative integer.

### Output:

Return a string denoting the largest possible number after arranging the elements of the array.

## Examples:

### Example 1:

**Input:**

```python
n = 5
arr[] = {"3", "30", "34", "5", "9"}
```

**Output:**

```python
"9534330"
```

**Explanation:**
Given numbers are {"3", "30", "34", "5", "9"}. The arrangement "9534330" gives the largest value.

### Example 2:

**Input:**

```python
n = 4
arr[] = {"54", "546", "548", "60"}
```

**Output:**

```python
"6054854654"
```

**Explanation:**
Given numbers are {"54", "546", "548", "60"}. The arrangement "6054854654" gives the largest value.

## Constraints:

- 1 <= n <= 10^5
- 0 <= len(arr[i]) <= 18
- Sum of all the elements of the array is greater than 0.

## Note:

- Your task is to implement the function `printLargest(arr: List[str]) -> str` to solve the problem.
- Do not read input or print anything. The function should take the array `arr[]` as an input argument and return the required answer.
- Your solution should have an expected time complexity of O(n\*log(n)).
- Your solution should have an expected auxiliary space complexity of O(n).

## Python Solution

```python
from functools import cmp_to_key

class Solution:
    def printLargest(self, n, array):
        def custom_compare(x, y):
            xy = x + y
            yx = y + x
            return (xy > yx) - (xy < yx)

        array.sort(key=cmp_to_key(custom_compare), reverse=True)

        return "".join(map(str, array))

```
