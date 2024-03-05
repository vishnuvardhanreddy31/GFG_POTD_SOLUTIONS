# Maximum Index

## 05-03-2024

**Problem Statement:**

Given an array `a` of `n` positive integers. The task is to find the maximum of `j - i` subjected to the constraint of `a[i] < a[j]` and `i < j`.

**Example:**

- Input:
  - `n = 2`
  - `a[] = {1, 10}`
- Output:
  - `1`
- Explanation:

  - `a[0] < a[1]` so `(j-i)` is `1-0 = 1`.

- Input:
  - `n = 9`
  - `a[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}`
- Output:
  - `6`
- Explanation:
  - In the given array `a[1] < a[7]` satisfying the required condition (`a[i] < a[j]`) thus giving the maximum difference of `j - i` which is `6(7-1)`.

**Your Task:**

The task is to complete the function `maxIndexDiff()` which finds and returns maximum index difference. Printing the output will be handled by driver code.

**Expected Time Complexity:** O(N)
**Expected Auxiliary Space:** O(N)

**Constraints:**

- 1 ≤ n ≤ 10^6
- 0 ≤ a[i] ≤ 10^9

## Python Solution

```python
class Solution:
    # Function to find the maximum index difference.
    def maxIndexDiff(self, a, n):
        if n == 1:
            return 0
        ans = -1
        lmin = [0] * n
        rmax = [0] * n
        lmin[0] = a[0]
        for i in range(1, n):
            lmin[i] = min(lmin[i - 1], a[i])
        rmax[n - 1] = a[n - 1]
        for j in range(n - 2, -1, -1):
            rmax[j] = max(rmax[j + 1], a[j])
        i, j = 0, 0
        while i < n and j < n:
            if lmin[i] <= rmax[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1
        return ans
```
