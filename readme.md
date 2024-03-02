# First Element to Occur K Times

## 02-03-2024

## Problem Statement:

Given an array of `n` integers, find the first element that occurs at least `k` number of times.

### Input:

- `n` (1 <= n <= 10^4): Size of the array.
- `k` (1 <= k <= 100): Minimum number of occurrences required.
- `a[]`: An array of integers where each element (1 <= a[i] <= 200) represents an integer.

### Output:

Return the first element that occurs at least `k` times. If no such element is found, return -1.

## Examples:

### Example 1:

```plaintext
Input:
n = 7, k = 2
a[] = {1, 7, 4, 3, 4, 8, 7}

Output:
4

Explanation:
Both 7 and 4 occur 2 times. However, 4 is the first element that occurs twice. At index 4, the element 4 has occurred twice, whereas 7 appeared twice at index 6.
```

### Example 2:

```plaintext
Input:
n = 10, k = 3
a[] = {3, 1, 3, 4, 5, 1, 3, 3, 5, 4}

Output:
3

Explanation:
Here, 3 is the only number that appeared 3 times in the array.
```

## Constraints:

- 1 <= n <= 10^4
- 1 <= k <= 100
- 1 <= a[i] <= 200

## Note:

- Your task is to implement the function `firstElementKTime` to solve the problem.
- Do not read input or print anything. The function should take the array `a[]`, its size `n`, and an integer `k` as input arguments and return the required answer.
- If the answer is not present in the array, return -1.

## Expected Time Complexity:

O(n)

## Expected Auxiliary Space:

O(n)

## Python Solution

```python
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        no_ones=0
        for i in s:
            if i=='1':
                no_ones+=1
        ans=''
        for i in range(no_ones-1):
            ans+='1'
        if no_ones!=1:
            remaining=len(s)-no_ones
            for i in range(remaining):
                ans+='0'
            ans+='1'
            return ans
        else:
            for i in range(len(s)-1):
                ans+='0'
            ans+='1'
            return ans

```
