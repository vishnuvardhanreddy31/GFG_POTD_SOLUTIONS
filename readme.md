# Generalised Fibonacci numbers

## 12-03-2024

## Python Solution

```python
class Solution:
    def multiply(self, A, B, m):
        size = len(A)
        result = [[0] * size for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    result[i][j] += A[i][k] * B[k][j]
                    result[i][j] %= m

        return result

    def genFibNum(self, a, b, c, n, m):
        if n <= 2:
            return 1 % m

        mat = [[a, b, 1], [1, 0, 0], [0, 0, 1]]
        res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        n -= 2

        while n > 0:
            if n & 1:
                res = self.multiply(res, mat, m)
            mat = self.multiply(mat, mat, m)
            n >>= 1

        return (res[0][0] + res[0][1] + c * res[0][2]) % m

```
