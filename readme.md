# Peak Element

## 01-03-2024

## Problem Description

Given an array of integers `arr[]` of size `n`, find its peak element. An element is considered to be peak if its value is greater than or equal to the values of its adjacent elements (if they exist). The array is guaranteed to be in ascending order before the peak element and in descending order after it.

## Example

### Example 1

**Input:**

```
n = 3
arr[] = {1, 2, 3}
```

**Peak Element's Index:** 2

**Output:** 1

**Explanation:** If the index returned is 2, then the output printed will be 1. Since `arr[2] = 3` is greater than its adjacent elements, and there is no element after it, we can consider it as a peak element. No other index satisfies the same property.

### Example 2

**Input:**

```
n = 3
arr[] = {3, 4, 2}
```

**Peak Element's Index:** 1

**Output:** 1

**Explanation:** If the index returned is 1, then the output printed will be 1. Since `arr[1] = 4` is greater than its adjacent elements, and there is no element after it, we can consider it as a peak element. No other index satisfies the same property.

## Your Task

You don't have to read input or print anything. Complete the function `peakElement()` which takes the array `arr[]` and its size `n` as input parameters and returns the index of the peak element.

**Expected Time Complexity:** O(log(n)).

**Expected Auxiliary Space:** O(1)

## Constraints

- 1 ≤ n ≤ 10^5
- 1 ≤ arr[i] ≤ 10^6

```python
class Solution:
    def peakElement(self,arr, n):
        # Code here
        left,right=0,n-1
        while left<right:
            mid=left+(right-left)//2

            if arr[mid]>arr[mid+1]:
                right=mid

            else:
                left=mid+1
        return left


```
