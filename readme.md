# Play With OR

## 27-02-2024

## Description

Given an array `arr[]` of length `n`, the task is to reconstruct the array in-place. Each element `arr[i]` after reconstruction will become `arr[i] OR arr[i+1]`, where `OR` is the bitwise OR operation. If for some `i`, `i+1` does not exist, then `arr[i]` remains unchanged.

## Example

### Example 1:

#### Input:

```
n = 5
arr[] = {10, 11, 1, 2, 3}
```

#### Output:

```
11 11 3 3 3
```

#### Explanation:

- At index 0, `arr[0] OR arr[1] = 11`
- At index 1, `arr[1] OR arr[2] = 11`
- At index 2, `arr[2] OR arr[3] = 3`
- ...
- At index 4, No element is left, so it will remain as it is.

New Array will be `{11, 11, 3, 3, 3}`.

### Example 2:

#### Input:

```
n = 4
arr[] = {5, 9, 2, 6}
```

#### Output:

```
13 11 6 6
```

#### Explanation:

- At index 0, `arr[0] OR arr[1] = 13`
- At index 1, `arr[1] OR arr[2] = 11`
- At index 2, `arr[2] OR arr[3] = 6`
- At index 3, No element is left, so it will remain as it is.

New Array will be `{13, 11, 6, 6}`.

## Your Task

You are required to implement the function `game_with_number()`, which takes an array `arr`, representing values at each index, and the size of the array `n`. The function should modify the elements of the same array `arr[]` in-place by replacing them with the values obtained by performing the bitwise OR operation on consecutive elements.

## Constraints

- `1 ≤ n ≤ 10^5`
- `1 ≤ arr[i] ≤ 10^7`

## Expected Complexity

- Expected Time Complexity: `O(n)`
- Expected Auxiliary Space: `O(1)`
-

## Python Solution

```python

class Solution:
    def game_with_number (self, arr,  n) :
        #Complete the function
        for i in range(n - 1):
            arr[i] = arr[i] | arr[i + 1]
        return arr

```
