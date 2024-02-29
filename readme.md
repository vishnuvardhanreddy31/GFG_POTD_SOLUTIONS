# Sum of Bit Differences

## 29-02-2024

## Problem Description

Given an array of integers `arr[]` containing `n` elements, find the sum of bit differences between all pairs of elements in the array. The bit difference of a pair (x, y) is the count of different bits at the same positions in the binary representations of x and y. Note that (x, y) and (y, x) are considered two separate pairs.

### Example

#### Example 1:

Input:

```
n = 2
arr[] = {1, 2}
```

Output:

```
4
```

Explanation:
All possible pairs of the array are (1, 1), (1, 2), (2, 1), (2, 2).
Sum of bit differences = 0 + 2 + 2 + 0 = 4

#### Example 2:

Input:

```
n = 3
arr[] = {1, 3, 5}
```

Output:

```
8
```

Explanation:
All possible pairs of the array are (1, 1), (1, 3), (1, 5), (3, 1), (3, 3), (3, 5), (5, 1), (5, 3), (5, 5).
Sum of bit differences = 0 + 1 + 1 + 1 + 0 + 2 + 1 + 2 + 0 = 8

### Constraints

- 1 <= n <= 10^5
- 1 <= arr[i] <= 10^5

## Complexity Analysis

- Expected Time Complexity: O(n)
- Expected Auxiliary Space: O(1)

## Python Solution

```python

# User function Template for python3
class Solution:
    def sumBitDifferences(self, arr, n):
        ans = 0
        for i in range(0, 32):
            count = 0
            for j in range(n):
                if (arr[j] & (1 << i)):
                    count += 1
            ans += (count * (n - count) * 2)

        return ans
```
