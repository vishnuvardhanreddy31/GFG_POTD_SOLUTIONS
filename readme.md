# Divisible By Eight

## 28-02-2024

## Problem Statement

Given a string representation of a decimal number `s`, check whether it is divisible by 8.

## Example

### Example 1:

**Input:**

```
s = "16"
```

**Output:**

```
1
```

**Explanation:**
The given number is divisible by 8, so the driver code prints 1 as the output.

### Example 2:

**Input:**

```
s = "54141111648421214584416464555"
```

**Output:**

```
-1
```

**Explanation:**
Given Number is not divisible by 8, so the driver code prints -1 as the output.

## Your Task

You don't need to read input or print anything. Your task is to complete the function `DivisibleByEight(s)` which takes a string `s` as the input and returns `1` if the number is divisible by 8, else it returns `-1`.

## Constraints

- 1 <= Number represented by the string `s` < 10^6

## Note

- Expected Time Complexity: O(1).
- Expected Auxillary Space: O(1).
-

```python

class Solution:
    def DivisibleByEight(self, s):
        # Remove non-numeric characters from the string
        s = ''.join(c for c in s if c.isdigit())

        # Check if the cleaned string is empty
        if not s:
            return -1  # If the string becomes empty after removing non-numeric characters, it's not divisible by 8

        # Check if the entire string is less than 4 digits
        if len(s) < 4:
            if int(s) % 8 == 0:
                return 1  # divisible by 8
            else:
                return -1  # not divisible by 8
        else:
            # Check the last three digits of the cleaned string
            num = int(s[-3:])
            if num == 0 or num % 8 == 0:
                return 1  # divisible by 8
            else:
                return -1  # not divisible by 8
```
