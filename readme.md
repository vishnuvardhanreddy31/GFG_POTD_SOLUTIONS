# Maximum Sum Problem

## 24-02-23

## Problem Description

A number `n` can be broken into three parts `n/2`, `n/3`, and `n/4` (consider only the integer part). Each number obtained in this process can be divided further recursively. Find the maximum sum that can be obtained by summing up the divided parts together. Note: It is possible that we don't divide the number at all.

## Examples

### Example 1:

**Input:**

```
n = 12
```

**Output:**

```
13
```

**Explanation:**
Break n = 12 into three parts {12/2, 12/3, 12/4} = {6, 4, 3}, now current sum is = (6 + 4 + 3) = 13. Further breaking 6, 4, and 3 into parts will produce a sum less than or equal to 6, 4, and 3 respectively.

### Example 2:

**Input:**

```
n = 24
```

**Output:**

```
27
```

**Explanation:**
Break n = 24 into three parts {24/2, 24/3, 24/4} = {12, 8, 6}, now the current sum is = (12 + 8 + 6) = 26. But recursively breaking 12 would produce a value of 13. So our maximum sum is 13 + 8 + 6 = 27.

## Your Task

You don't need to read input or print anything. Your task is to complete the function `maxSum()` which accepts an integer `n` and returns the maximum sum.

## Constraints

- 0 <= n <= 10^6

## Expected Complexity

- Expected Time Complexity: O(n)
- Expected Auxiliary Space: O(n)

# Python Solution

```python
class Solution:
    def maxSum(self, n):
        dp = [-1 for _ in range(n + 1)]

        def helper(n, dp):
            if n == 0 or n == 1:
                return n
            if dp[n] != -1:
                return dp[n]
            else:
                dp[n] = max(n, helper(n // 3, dp) + helper(n // 2, dp) + helper(n // 4, dp))
                return dp[n]

        return helper(n, dp)
```
