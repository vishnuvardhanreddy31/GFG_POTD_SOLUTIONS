# Reach a Given Score

## 25-02-2024

## Problem Description

Consider a game where a player can score 3, 5, or 10 points in a move. Given a total score `n`, find the number of distinct combinations to reach the given score.

## Examples

### Example 1:

**Input:**

```
n = 10
```

**Output:**

```
2
```

**Explanation:**
There are two ways {5,5} and {10}.

### Example 2:

**Input:**

```
n = 20
```

**Output:**

```
4
```

**Explanation:**
There are four possible ways. {5,5,5,5}, {3,3,3,3,3,5}, {10,10}, {5,5,10}.

## Your Task

You don't need to read input or print anything. Your task is to complete the function `count()` which takes `n` as an input parameter and returns the answer to the problem.

## Constraints

- 1 ≤ n ≤ 10^6

## Expected Complexity

- Expected Time Complexity: O(n)
- Expected Auxiliary Space: O(n)

# Python Solution

```python
class Solution:
    def count(self, n: int) -> int:
        ways = [0] * (n + 1)

        # Base case (If given value is 0)
        ways[0] = 1

        # Consider all possible moves
        moves = [3, 5, 10]
        for i in range(3):
            for j in range(moves[i], n+1):
                ways[j] += ways[j - moves[i]]

        return ways[n]
```
