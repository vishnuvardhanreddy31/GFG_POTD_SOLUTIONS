## 23-02-24

# Buy and Sell a Share at most twice

## Problem Statement:

In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is allowed to make at most 2 transactions in a day, the second transaction can only start after the first one is complete (buy->sell->buy->sell). The stock prices throughout the day are represented in the form of an array of prices.

Given an array `price` of size `n`, find out the maximum profit that a share trader could have made.

### Example:

#### Input:

```
n = 6
prices[] = {10,22,5,75,65,80}
```

#### Output:

```
87
```

Explanation: Trader earns 87 as sum of 12, 75 Buy at 10, sell at 22, Buy at 5 and sell at 80.

## Implementation:

Complete the function `maxProfit()` which takes an integer array `price` as the only argument and returns an integer, representing the maximum profit, if only two transactions are allowed.

### Constraints:

- 1 <= n <= 10^5
- 1 <= price[i] <= 10^5

### Expected Time Complexity:

O(n)

## Expected Space Complexity:

O(n)

## Solution

```python

from typing import List


class Solution:
    def maxProfit(self, n : int, price : List[int]) -> int:

        profit = [0]*n

        max_price = price[n-1]

        for i in range(n-2, 0, -1):

            if price[i] > max_price:
                max_price = price[i]

            profit[i] = max(profit[i+1], max_price - price[i])

        min_price = price[0]

        for i in range(1, n):

            if price[i] < min_price:
                min_price = price[i]

            profit[i] = max(profit[i-1], profit[i]+(price[i]-min_price))

        result = profit[n-1]

        return result

```
